#include "create_graph.cc"
#include "shortest_distance.cc"
#include <utility>

using std::pair;

/**
 * Find shortest path (with BFS) for every query and print through stdout
 */
void answer_queries(map<string, Node>& graph, const vector<pair<string, string>>& queries){
    for(auto& q : queries){
        int distance = shortest_distance(graph.at(q.first), graph.at(q.second));
        if(distance > 0)
            cout << distance << endl;
        else cout << "Impossible" << endl;
    }
}

int main(){
    vector<string>::size_type nr_words;
    int nr_queries;
    cin >> nr_words;
    cin >> nr_queries;

    map<string, Node> graph = create_graph(nr_words);

    auto& n = graph.at("baccc");
    cout << "\n" << n << endl;
    for(auto e : n.neighbors){
        cout << e << endl;
    } cout << endl;

    // Read queries
    string from;
    string to;
    vector<pair<string, string>> queries;
    for(int i = 0; i != nr_queries; ++i){
        cin >> from >> to;
        queries.emplace_back(from, to);
    }

    answer_queries(graph, queries);
}

