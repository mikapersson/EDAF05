#include "node.h"
#include <queue>
#include <functional>  // std::greater
#include <tuple>  // std::tie

/**
 * Returns the minimum distance with the help of Prim's algorithm
 * 
 * @param graph in which we want to compute the minimum distance
 * @return minimum distance
 */
int minimum_distance(const vector<Node*>& graph){
    typedef pair<int, Node*> next;

    int min_distance{0};
    Node* start = graph[0];  // start can be an arbitrary node
    std::priority_queue<next, vector<next>, std::greater<next>> pq;
    pq.emplace(0, start);

    int distance;
    Node* closest;
    while(pq.size() > 0){
        std::tie(distance, closest) = pq.top();
        pq.pop();  // pop() doesn't return the top element
        
        if(!closest->visited){
            min_distance += distance;
            closest->visited = true;
            
            for(const auto& neighbor : closest->neighbors){
                if(!neighbor.first->visited)
                    pq.emplace(neighbor.second, neighbor.first);
            }
        }
    }
    return min_distance;
}