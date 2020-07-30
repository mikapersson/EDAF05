#include <queue>
#include "node.h"

using std::queue;

int count_edges(Node& node){
    int count{0};
    while(node.previous != nullptr){
        node = *node.previous;
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
int shortest_distance(Node from, Node to){  //
    if(from.word == to.word)
        return 0;

    from.visited = true;
    queue<Node> q;
    q.push(from);
    
    while(q.size() > 0){
        Node next = q.front();  // front() doesn't remove the node from q
        q.pop();                // remove the node from q
        for(auto& neighbor : next.neighbors){
            neighbor.visited = true;
            q.push(neighbor);
            neighbor.previous = &next;  // not dynamic allocation
            if(neighbor.word == to.word)
                return count_edges(neighbor);
        }
    return 0;  // no path
    }
}
