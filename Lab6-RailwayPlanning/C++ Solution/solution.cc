#include "setup.cc"

int main(){
    int nr_nodes, nr_edges, capacity, nr_routes;
    cin >> nr_nodes >> nr_edges >> capacity >> nr_routes;

    node_vector nodes;
    edge_vector edges;
    route_vector routes;

    std::tie(nodes, edges, routes) = setup(nr_nodes, nr_edges, nr_routes);

    return 0;
}