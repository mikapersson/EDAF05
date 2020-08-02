#include "setup.cc"
#include <algorithm>

typedef vector<Node*> Graph;

Graph create_graph(node_vector& nodes, edge_vector& edges, route_vector& routes);
void free_nodes(node_vector& nodes);
void free_edges(edge_vector& edges);

int main(){
    int nr_nodes, nr_edges, capacity, nr_routes;
    cin >> nr_nodes >> nr_edges >> capacity >> nr_routes;

    node_vector nodes;
    edge_vector edges;
    route_vector routes;
    std::tie(nodes, edges, routes) = setup(nr_nodes, nr_edges, nr_routes);

    Graph graph = create_graph(nodes, edges, routes);  // initial graph without route edges


    // Free dynamically allocated memory (raw pointers)
    free_nodes(nodes);
    free_edges(edges);

    return 0;
}

Graph create_graph(node_vector& nodes, edge_vector& edges, route_vector& routes){
    Graph graph(nodes.size());  // elements default initialized to nullptr



    return graph;
}

void free_nodes(node_vector& nodes){
    for(auto& n : nodes){
        delete n;
    }
}

void free_edges(edge_vector& edges){
    for(auto& e : edges){
        delete e;
    }
}