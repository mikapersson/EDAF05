#include <queue>
#include "node.h"
#include <iostream>

using std::queue;
using namespace std;

int count_edges(const Node& node){
    cout << "Entered counting: " << node.word;
    int count{0};
    Node* temp_ptr = node.previous;
    while(temp_ptr != nullptr){
        cout << " -> " << temp_ptr->word;
        temp_ptr = temp_ptr->previous;
        ++count;
    }
    cout << ": ";
    return count;
}

/**
 * Finds the shortest path from node 'from' to node 'to' using BFS
 * 
 * @param from
 * @param to
 * @return distance between the two nodes
 */ 
int shortest_distance(Node from, Node to){  
    cout << "\nNew distance" << endl;
    for(const auto& i : from.neighbors){
        cout << *i << endl;
    }
    
    if(from.word == to.word)
        return 0;

    from.visited = true;
    queue<Node*> q;
    q.push(&from);
    
    while(q.size() > 0){  
        Node* next(q.front());  // front() doesn't remove the node from q
        q.pop();                // remove the node from q (pop doesn't return front())
        cout << "\tpopped " << next->word << endl;
        for(auto& neighbor : next->neighbors){  
            cout << "\t\tneighbor " << neighbor->word << endl;
            if(neighbor->visited == false){
                neighbor->visited = true;
                neighbor->previous = next;  // not dynamic allocation
                q.push(neighbor);
                cout << "\t\t\tpushed " << neighbor->word << endl;
                if(neighbor->word == to.word)
                    return count_edges(*neighbor);
            } else {
                cout << "\t\t\talready visited" << endl;
            }
        }
    }
    
    return 0;  // no path
}
