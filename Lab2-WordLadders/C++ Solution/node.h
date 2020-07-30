#ifndef NODE_H
#define NODE_H

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
    Node(const string& w) : word(w), visited(false), previous(nullptr) {}
    Node(const Node& other) : word(other.word), visited(other.visited),
                            neighbors(other.neighbors), previous(other.previous) {}
    Node& operator=(const Node& other) {  // Copy assignment
        word = other.word;
        visited = other.visited;
        neighbors = other.neighbors;
        previous = other.previous;
        return *this;
    }

    string word;
    bool visited;
    vector<Node*> neighbors;
    Node* previous;

    friend ostream& operator<<(ostream& o, const Node& node) { 
        o << "Node " << node.word << " with neighbors: ";
        for(const auto& nghbr : node.neighbors){
            o << nghbr->word << " ";
        }

        return o;
    }
};

#endif