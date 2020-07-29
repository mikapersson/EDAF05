#include <map>
#include <algorithm>
#include "node.h"

using std::cin;
using std::map;
using std::ostream;
using std::all_of;

// Used as predicate in all_of-function in edge_exists method below
bool boolean(const bool& b){
    return b;
}

/**
 * Checks if there exists a edge/path (see lab pdf) from string 
 * 'from' to string 'to' (both are five letter words)
 * 
 * @param from the string from which we examine if an edge exists
 * @param to   the string to -||-
 * @return     true if there exists an edge between the words, otherwise false
 */
bool edge_exists(const string& from, string to) {
    vector<bool> exist;
    for(auto char_itr = from.begin()+1; char_itr != from.end(); ++char_itr){
        auto pos = to.find(*char_itr);
        if(pos != string::npos){
            exist.emplace_back(true);
            to.erase(pos, 1);
        } else {
            exist.emplace_back(false);
        }
    }
    return all_of(exist.begin(), exist.end(), boolean);
}


/**
 * Creates a directed graph from input through stdin
 * 
 * @param nr_words number of words/nodes in graph 
 * @return directed graph  
 */
map<string, Node> create_graph(const int& nr_words){
    map<string, Node> graph;

    // Read words into a vector
    vector<string> words;
    words.resize(nr_words);
    string temp_word;
    for(vector<string>::size_type i = 0; i != nr_words; ++i){
        cin >> temp_word;
        words[i] = temp_word;
    }

    // Create skeleton for graph (Node values will not have any neighbors yet)
    for(const auto& w : words){
        graph.emplace(w, Node(w));
    }

    // Add neighbors to each node in the graph
    for(auto from = graph.begin(); from != graph.end(); ++from) {
        for(auto to = graph.begin(); to != graph.end(); ++to) {
            if(edge_exists(from->first, to->first) && from != to)
                from->second.neighbors.emplace_back(to->first);
        }
    }

    /*
    // Verify that the graph was correctly built
    for(const auto& p : graph){
        cout << p.second << endl;
    }*/

    return graph;
}
