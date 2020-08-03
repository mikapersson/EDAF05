#ifndef NODE_H
#define NODE_H

#include <iostream>
#include <vector>
struct Edge;  // forward declaration

struct Node{
    /*
    friend std::ostream& operator<<(std::ostream& o, const Node& n){
        o << "Node " << n.index << std::boolalpha << ", visited=" << n.visited <<
            ", edges: ";
        for(const auto& e : n.edges){
            o << "\t" << *e;
        }
        return o;
    }*/

    Node(const int&);
    int index;
    bool visited;
    Node* previous_node;
    Edge* previous_edge;
    std::vector<Edge*> edges;

    void print_node();
};

#endif