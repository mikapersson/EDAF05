#include "node.h"

using std::cin;

/**
 * Creates the graph corresponding to the input (through stdin)
 * 
 * @return graph represented by an adjacency list
 */
vector<Node*> make_graph() {
    int nr_nodes;
    int nr_edges;
    cin >> nr_nodes >> nr_edges;

    // Create vector/graph containing all nodes
    vector<Node*> graph;  // adjacency list for graph implementation
    graph.reserve(nr_nodes);
    for(int i = 0; i != nr_nodes; ++i) {
        graph.emplace_back(new Node(i+1));
    }

    // Read edges/pairs into graph
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

