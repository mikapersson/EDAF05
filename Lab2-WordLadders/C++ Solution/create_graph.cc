#include <map>
#include <algorithm>
#include "node.h"
#include <utility>

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

void print_graph(const map<string, Node>& graph) {
    for(const auto& p : graph){
        cout << p.second << endl;
    } cout << endl;
}


/**
 * Creates a directed graph from input through stdin
 * 
 * @param nr_words number of words/nodes in graph 
 * @return directed graph  
 */
std::pair<map<string, Node*>, vector<Node*>> create_graph(const vector<Node>::size_type& nr_words){
    map<string, Node*> graph;

    // Read words/nodes into a vector
    vector<Node*> node_ptrs;
    node_ptrs.resize(nr_words);
    string temp_word;
    for(vector<string>::size_type i = 0; i != nr_words; ++i){
        cin >> temp_word;
        Node* new_node = new Node(temp_word);
        node_ptrs[i] = new_node;
    }

    // Add neighbors to nodes
    for(auto from : node_ptrs) {
        for(auto to : node_ptrs) {
            if(edge_exists(from->word, to->word) && from->word != to->word)
                from->neighbors.push_back(to);
        }
    }
    

    // Add nodes to graph
    for(const auto& node_ptr : node_ptrs){
        graph.emplace(node_ptr->word, node_ptr);
    }
    
    
    // Verify that the graph was correctly built
    //print_graph(graph);

    return std::make_pair(graph, node_ptrs);
}
