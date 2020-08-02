#ifndef NODE_H
#define NODE_H

#include <iostream>
#include <vector>
struct Edge;  // forward declaration

struct Node{
    friend std::ostream& operator<<(std::ostream& o, const Node& n){
        return o << "Node " << n.index << std::boolalpha << ", visited=" << n.visited;
    }   
    Node(const int&);
    int index;
    bool visited;
    Node* previous_node;
    Edge* previous_edge;
    std::vector<Edge*> edges;
};

#endif