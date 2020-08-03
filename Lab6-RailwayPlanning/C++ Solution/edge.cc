#include "edge.h"
#include "node.h"

using std::cout;
using std::endl;

Edge::Edge(Node* n1, Node* n2, const int& cap) : destination1(n1), destination2(n2), capacity(cap),
                                            front_flow(0), back_flow(0) {}

/**
 * Get capacity of edge towards node 'n'
 */ 
int Edge::get_capacity(const Node* n){
    if(n == destination2)
        return capacity - front_flow;
    else return capacity - back_flow;
}

/**
 * Increase flow towards node 'n' with 'delta'
 */
void Edge::update_flow(const Node* n, const int& delta){
    if(n == destination2){
        front_flow += delta;
        back_flow -= delta; 
    } else {
        back_flow += delta;
        front_flow -= delta;
    }
}

/**
 * Checks if flow = capacity towards node 'n', returns true if so, otherwise false
 */ 
bool Edge::is_full(const Node* n){
    if(n == destination2)
        return capacity == front_flow;
    else return capacity == back_flow;
}

void Edge::print_edge(){
    cout << "Edge from " << destination1->index << " to " << destination2->index << 
            " with capacity " << capacity << ", front flow " << front_flow <<
            " and back flow " << back_flow;
}