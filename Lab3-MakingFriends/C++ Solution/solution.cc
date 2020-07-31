#include "make_graph.cc"
#include <tuple>  // std::tie
#include "prim.cc"

using std::tie;
using std::cout;

/**
 * Can be used to verify that the graph was somehow correctly built (but use debugging instead)
 */
void print_graph(const vector<Node*>& graph){
    for(const auto& n : graph) {
        cout << *n << endl;
    }
}

int main(){
    vector<Node*> graph = make_graph();

    int min_distance = minimum_distance(graph);
    cout << min_distance << endl;

    // Free memory
    for(auto& p : graph){
        delete p;
    }

    return 0;
}
