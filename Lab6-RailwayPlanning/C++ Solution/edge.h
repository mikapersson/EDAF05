#ifndef EDGE_H
#define EDGE_H


struct Node;  // forward declaration

struct Edge{
    Edge(Node* n1, Node* n2, const int& cap);
    int get_capacity(const Node* n);
    void update_flow(const Node* n, const int& delta);
    bool is_full(const Node* n);

    Node* destination1;
    Node* destination2;
    int capacity;
    int front_flow;
    int back_flow;
};

#endif