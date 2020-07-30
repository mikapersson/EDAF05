#include <queue>
#include "node.h"
#include <iostream>

using std::queue;
using namespace std;

int count_edges(Node& node){
    cout << "Entered counting: " << node.word;
    int count{0};
    while(node.previous != nullptr){
        node = *node.previous;
        cout << " <- " << node.word;
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
int shortest_distance(Node from, Node to){  // call by value -> no need to reset graph every call
    cout << endl;
    cout << "Finding distance from " << from.word << " to " << to.word << ": " << endl;
    if(from.word == to.word)
        return 0;

    from.visited = true;
    queue<Node> q;
    q.push(from);
    
    while(q.size() > 0){
        Node next(q.front());  // front() doesn't remove the node from q
        q.pop();                // remove the node from q (pop doesn't return front())
        cout << "\tpopped " << next.word << endl;
        for(auto& neighbor : next.neighbors){
            cout << "\t\tneighbor " << neighbor->word << endl;
            if(neighbor->visited == false){
                neighbor->visited = true;
                neighbor->previous = &next;  // not dynamic allocation
                q.push(*neighbor);
                cout << "\t\t\tpushed " << neighbor->word << endl;
                if(neighbor->word == to.word)
                    return count_edges(*neighbor);
            }
        }
    }
    
    return 0;  // no path
}
