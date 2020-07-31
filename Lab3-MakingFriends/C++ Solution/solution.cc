#include "make_graph.cc"
#include <tuple>  // std::tie
#include "prim.cc"

using std::tie;
using std::cout;

void print_graph(const vector<Node*>& graph){
    for(const auto& n : graph) {
        cout << *n << endl;
    }
}

int main(){

    vector<Node*> graph;
    graph = make_graph();


    // Verifying that the graph was correctly built 
    // (though this can be checked while debugging)
    print_graph(graph);

    int min_distance = minimum_distance(graph);
    cout << min_distance << endl;

    // Free memory
    for(auto& p : graph){
        delete p;
    }

    return 0;
}