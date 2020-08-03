#include "edge.h"
#include "node.h"
#include "setup.cc"
#include <queue>
#include <limits>

// Function used in ford_fulkerson()
bool find_path(Graph& graph, Node* source, Node* sink);

/**
 * Finds the maximal flow from source_index to sink_index in graph
 */ 
int ford_fulkerson(Graph& graph, const int& source_index, const int& sink_index){
    int new_flow(0);

    Node* source = graph[source_index];
    if(source == nullptr)  // if the source node doesn't yet belong to the graph
        return 0;

    Node* sink = graph[sink_index];
    if(sink == nullptr)  // if the sink node -||-
        return 0;

    bool path_exists = find_path(graph, source, sink);
    while(path_exists){
        int delta = std::numeric_limits<int>::max();
        Node* temp_node = sink;

        // Find minimal capacity on the path found
        while(temp_node != source){
            delta = std::min(delta, temp_node->previous_edge->get_capacity(temp_node));
            temp_node = temp_node->previous_node;
        }

        // Update the flow through the found path with 'delta'
        new_flow += delta;
        temp_node = sink;
        while(temp_node != source){
            temp_node->previous_edge->update_flow(temp_node, delta);
            temp_node = temp_node->previous_node;
        }

        path_exists = find_path(graph, source, sink);
    }
    
}

/**
 * Finds a path from source to sink using BFS 
 */
bool find_path(Graph& graph, Node* source, Node* sink){

}