#include "node.h"
#include "edge.h"

using std::cout;
using std::endl;

Node::Node(const int& i) : index(i), visited(false), previous_node(nullptr), previous_edge(nullptr) {}

void Node::print_node(){
    cout << "Node " << index << std::boolalpha << ", visited=" << visited <<
            ", edges: ";
        for(const auto& e : edges){
            cout << "\n\t";
            e->print_edge();
        }
        cout << endl;
}