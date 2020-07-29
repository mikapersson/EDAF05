#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;
using std::cout;
using std::endl;
using std::ostream;

/**
 * Class describing a node, a five letter word with edges 
 * to other nodes (represented by a vector<Node>) that is.
 */
struct Node {  // members are public by default
    Node() = default;
    Node(const string& w) : word(w), visited(false) {}
    string word;
    bool visited;
    vector<Node> neighbors;
    Node* previous;

    friend ostream& operator<<(ostream& o, const Node& node) { 
        o << "Node " << node.word << " with neighbors: ";
        for(const auto& nghbr : node.neighbors){
            o << nghbr.word << " ";
        }

        return o;
    }
};