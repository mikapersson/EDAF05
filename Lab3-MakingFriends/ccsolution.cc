#include "ccprim.h"
#include <iostream>

using namespace std;

int main(){

    //Choose and run algorithm on input data
    bool prim = true;  //true = prim, false = kruskal
    if(prim){
        prims();
    } else {
        //runKruskals();
    }
    return 0;
}