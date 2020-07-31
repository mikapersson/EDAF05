#include "make_graph.cc"
#include <tuple>  // std::tie

using std::tie;

void print_graph(const vector<Node*>& graph){
    for(const auto& n : graph) {
        cout << *n << endl;
    }
}

int main(){

    vector<Node*> graph;
    graph = make_graph();


    // Verifying that the graph was correctly built
    print_graph(graph);

    // Free memory
    for(auto& p : graph){
        delete p;
    }

    return 0;
}