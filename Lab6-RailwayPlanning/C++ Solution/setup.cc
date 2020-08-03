#include <iostream>
#include <vector>
#include "node.h"
#include "edge.h"
#include <tuple>

using std::cin;
using std::vector;
using std::cout;
using std::endl;

typedef vector<Node*> node_vector;
typedef vector<Edge*> edge_vector;
typedef vector<int> route_vector;  // must be vector to enable searching for content
typedef vector<Node*> Graph;

std::tuple<node_vector, edge_vector, route_vector> setup(const int& nr_nodes, const int& nr_edges, const int& nr_routes){
    // Create nodes
    node_vector nodes;
    for(int i = 0; i != nr_nodes; ++i){
        nodes.emplace_back(new Node(i));
    }
    
    // Create edges
    edge_vector edges;
    node_vector::size_type index1, index2;
    int capacity;

    for(int i = 0; i != nr_edges; ++i){
        cin >> index1 >> index2 >> capacity;
        Node* node1 = nodes[index1];
        Node* node2 = nodes[index2];
        edges.emplace_back(new Edge(node1, node2, capacity));
    }

    // Collect routes
    route_vector routes;
    for(int i = 0; i != nr_routes; ++i){
        int temp_route;
        cin >> temp_route;
        routes.emplace_back(temp_route);
    }

    return std::make_tuple(nodes, edges, routes);
}