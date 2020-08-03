#ifndef EDGE_H
#define EDGE_H

#include <iostream>

struct Node;  // forward declaration

struct Edge{
    /*
    friend std::ostream& operator<<(std::ostream& o, const Edge& e){
        o << "Edge from " << e.destination1->index << " to " << e.destination2->index << 
            " with capacity " << e.capacity;
        return o;
    }*/

    Edge(Node* n1, Node* n2, const int& cap);
    int get_capacity(const Node* n);
    void update_flow(const Node* n, const int& delta);
    bool is_full(const Node* n);

    Node* destination1;
    Node* destination2;
    int capacity;
    int front_flow;
    int back_flow;

    void print_edge();  
};

#endif