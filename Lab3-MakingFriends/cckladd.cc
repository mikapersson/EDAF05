#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <utility>
#include <limits>
#include <typeinfo>

using namespace std;

struct Friend{
    Friend(int id) : id{id} {}
    int id;
    vector<pair<int, int>> friends;
    int minDistance = numeric_limits<int>::max();
};

int main(){
    
    /*
    Friend f1(1);

    for(int i = 0; i != 5; ++i){
        f1.friends.push_back(make_pair(i+1, i*i));
    }
    for(auto &p : f1.friends){
        cout << p.first << " " << p.second << endl;
    }*/

    int N;
    int Q;
    cin >> N >> Q;

    cout << "N: " << N << ", Q: " << Q << endl;
    bool b = N == 2;
    cout << b << endl;


    return 0;
}