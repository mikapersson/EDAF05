#ifndef NODE_H
#define NODE_H

#include <vector>
class Edge;  // forward declaration

class Node{
    Node(const int&);
    int index;
    bool visited;
    Node* previous_node;
    Edge* previous_edge;
    std::vector<Edge*> edges;
};

#endif