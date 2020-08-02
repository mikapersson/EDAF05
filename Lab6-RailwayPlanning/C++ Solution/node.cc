#include "node.h"
#include "edge.h"

Node::Node(const int& i) : index(i), visited(false), previous_node(nullptr), previous_edge(nullptr) {}