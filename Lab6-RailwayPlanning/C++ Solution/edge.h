#ifndef EDGE_H
#define EDGE_H


struct Node;  // forward declaration

struct Edge{
    Edge(Node* n1, Node* n2, const int& cap);
    Node* destination1;
    Node* destination2;
    int capacity;
    int front_flow;
    int back_flow;
};

#endif