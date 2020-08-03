#include "edge.h"
#include "node.h"
#include <queue>
#include <limits>

typedef vector<Node*> Graph;

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

    bool path_exists = find_path(graph, source, sink);  // ERROR
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
    //cout << "\t" << new_flow << endl;
    return new_flow;
}

/**
 * Finds a path from source to sink using BFS 
 */
bool find_path(Graph& graph, Node* source, Node* sink){
    // Reset the nodes in 'graph'
    for(auto& n : graph){
        n->visited = false;
        n->previous_node = nullptr;
        n->previous_edge = nullptr;
    }

    bool path_exists = false;
    source->visited = true;
    std::queue<Node*> node_queue;
    node_queue.push(source);

    // While there is a potential path from 'source' to 'sink'
    while(node_queue.size() > 0 && !path_exists){
        Node* temp_node = node_queue.front();
        temp_node->visited = true;
        node_queue.pop();

        Node* next_node(nullptr);
        // Examine all edges from 'temp_node'
        for(auto& edge : temp_node->edges){
            if(edge->destination1 == temp_node)
                next_node = edge->destination2;
            else next_node = edge->destination1;

            // If the current edge is not full
            if(!(edge->is_full(next_node) || next_node->visited)){
                node_queue.push(next_node);
                next_node->previous_node = temp_node;
                next_node->previous_edge = edge;

                // If we've reached 'sink'
                if(next_node == sink){
                    path_exists = true;
                    break;
                }
            }
        }
    }
    return path_exists;
}