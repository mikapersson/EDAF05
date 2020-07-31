#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

using namespace std;

/**
 * Node class used in graph
 */
struct Node {
    Node(const int& n) : number(n) , visited(false) {}
    int number;
    bool visited;
    vector<pair<Node*, int>> neighbors;

    friend ostream& operator<<(ostream& o, const Node& n) {
        o << "Node " << n.number << boolalpha << ", visited = " << n.visited << ", neighbors:" << endl;
        for(const auto& e : n.neighbors){
            o << "\t" << e.first->number << " : " << e.second << endl;
        }
        return o;
    }
};

/**
 * Creates the graph corresponding to the input (through stdin)
 * 
 * @return graph represented by an adjacency list
 */
vector<Node*> make_graph() {
    int nr_nodes;
    int nr_edges;
    cin >> nr_nodes >> nr_edges;

    // Create vector containing all nodes
    vector<Node*> graph;  // adjacency list for graph implementation
    graph.reserve(nr_nodes);
    for(int i = 0; i != nr_nodes; ++i) {
        graph.emplace_back(new Node(i+1));
    }

    // Place nodes and read edges/pairs into graph
    int from;
    int to;
    int distance;
    for(int i = 0; i != nr_edges; ++i) {
        cin >> from >> to >> distance;
        graph[from - 1]->neighbors.emplace_back(graph[to - 1], distance);
        graph[to - 1]->neighbors.emplace_back(graph[from - 1], distance);  // undirected graph
    }

    return graph;
}

