#ifndef NODE_H
#define NODE_H

#include <vector>
#include <iostream>
#include <utility>

using std::vector;
using std::endl;
using std::ostream;
using std::pair;

/**
 * Node class used in graph
 */
struct Node {
    Node(const int& n) : number(n) , visited(false) {}
    int number;
    bool visited;
    vector<pair<Node*, int>> neighbors;

    friend ostream& operator<<(ostream& o, const Node& n) {
        o << "Node " << n.number << std::boolalpha << ", visited = " << n.visited << ", neighbors:" << endl;
        for(const auto& e : n.neighbors){
            o << "\t" << e.first->number << " : " << e.second << endl;
        }
        return o;
    }
};

#endif  // NODE_H