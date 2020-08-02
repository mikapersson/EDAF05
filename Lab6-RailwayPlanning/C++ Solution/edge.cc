#include "edge.h"
#include "node.h"

Edge::Edge(Node* n1, Node* n2, const int& cap) : destination1(n1), destination2(n2), capacity(cap) {}