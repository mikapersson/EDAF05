#include "setup.cc"
#include <algorithm>  // std::find
#include <utility>
#include "ford_fulkerson.cc"

using std::tie;

Graph create_graph(node_vector& nodes, edge_vector& edges, route_vector& routes);
std::pair<route_vector::size_type, int> max_flow(Graph& graph, const int& capacity,
                                const int& nr_nodes, edge_vector& edges, route_vector& routes);
void free_nodes(node_vector& nodes);
void free_edges(edge_vector& edges);
void print_graph(const Graph& graph);

int main(){
    int nr_nodes, nr_edges, capacity, nr_routes;
    cin >> nr_nodes >> nr_edges >> capacity >> nr_routes;

    node_vector nodes;
    edge_vector edges;
    route_vector routes;
    tie(nodes, edges, routes) = setup(nr_nodes, nr_edges, nr_routes);

    Graph graph = create_graph(nodes, edges, routes);  // initial graph without route edges
    route_vector::size_type nr_removed;
    int maxf;
    tie(nr_removed, maxf) = max_flow(graph, capacity, nr_nodes, edges, routes); 
    cout << nr_removed << " " << maxf << endl;
    

    // Free dynamically allocated memory (raw pointers)
    free_nodes(nodes);
    free_edges(edges);

    return 0;
}

Graph create_graph(node_vector& nodes, edge_vector& edges, route_vector& routes){
    Graph graph(nodes.size());  // elements default initialized to nullptr
    for(edge_vector::size_type i = 0; i != edges.size(); ++i){
        if(std::find(routes.begin(), routes.end(), i) == routes.end()){  // if the edge isn't included in 'routes'
            auto temp_edge = edges[i];  // pointer to an edge-object
            Node* from = temp_edge->destination1;
            int from_index = from->index;
            Node* to = temp_edge->destination2;
            int to_index = to->index;

            // Insert the new edge (including nodes) into the graph
            if(graph[from_index] == nullptr){
                from->edges.push_back(temp_edge);
                graph[from_index] = from;
            } else {
                graph[from_index]->edges.push_back(temp_edge);
            }

            if(graph[to_index] == nullptr) {  // undirected graph
                to->edges.push_back(temp_edge);
                graph[to_index] = to;
            } else {
                graph[to_index]->edges.push_back(temp_edge);
            }
        }
    }
    return graph;
}


/**
 * @return pair, first: number of edges that could be removed, second: max flow
 */ 
std::pair<route_vector::size_type, int> max_flow(Graph& graph, const int& capacity, 
                                    const int& nr_nodes, edge_vector& edges, route_vector& routes){
    Graph::size_type source_index(0);
    Graph::size_type sink_index(nr_nodes-1);

    // Add one route at a time to the graph and run FF algorithm for each iteration
    int max = ford_fulkerson(graph, source_index, sink_index);  // initial run
    
    while(max < capacity){
        int new_edge_index = routes.back();
        routes.pop_back();

        Edge* new_edge = edges[new_edge_index];
        Node* from = new_edge->destination1;
        int from_index = from->index;
        Node* to = new_edge->destination2;
        int to_index = to->index;

        if(graph[from_index] == nullptr){
            from->edges.push_back(new_edge);
            graph[from_index] = from;
        } else {
            graph[from_index]->edges.push_back(new_edge);
        }

        if(graph[to_index] == nullptr){  // undirected graph
            to->edges.push_back(new_edge);
            graph[to_index] = to;
        } else {
            graph[to_index]->edges.push_back(new_edge);
        }
        
        max += ford_fulkerson(graph, source_index, sink_index);
    }
    return std::make_pair(routes.size(), max);
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

// Verifying that the graph is correct
void print_graph(const Graph& graph){
    cout << "Printing graph..." << endl;
    for(const auto& e : graph){
        if(e != nullptr){
            e->print_node();
            cout << endl;
        }
    }
    cout << "...finished printing" << endl;
}