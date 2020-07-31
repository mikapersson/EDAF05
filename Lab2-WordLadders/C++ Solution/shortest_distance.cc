#include <queue>
#include "node.h"
#include <iostream>

using std::queue;
using namespace std;

int count_edges(const Node* node){
    int count{0};
    Node* temp_ptr = node->previous;
    while(temp_ptr != nullptr){
        temp_ptr = temp_ptr->previous;
        ++count;
    }
    return count;
}

/**
 * Finds the shortest path from node 'from' to node 'to' using BFS
 * 
 * @param from
 * @param to
 * @return distance between the two nodes
 */ 
int shortest_distance(Node* from, Node* to){      
    if(from->word == to->word)
        return 0;

    from->visited = true;
    queue<Node*> q;
    q.push(from);
    
    while(q.size() > 0){  
        Node* next(q.front());  // front() doesn't remove the node from q
        q.pop();                // remove the node from q (pop doesn't return front())
        for(auto& neighbor : next->neighbors){  
            if(neighbor->visited == false){
                neighbor->visited = true;
                neighbor->previous = next;  // not dynamic allocation
                q.push(neighbor);
                if(neighbor->word == to->word)
                    return count_edges(neighbor);
            } 
        }
    }
    return -1;  // no path
}
