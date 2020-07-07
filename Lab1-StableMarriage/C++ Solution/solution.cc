#include "read_data.cc" 
#include <tuple>         // std::tie
#include "gale_shapley.cc"
#include <map>

void print_people(const vector<Person>& people){
    cout << "\nPrinting people.." << endl;
    for(auto& p : people){
        cout << p << endl;
    }
    cout << "..finished!\n" << endl;
}
void print_people(const deque<Person>& people){
    cout << "\nPrinting people.." << endl;
    for(auto& p : people){
        cout << p << endl;
    }
    cout << "..finished!\n" << endl;
}

int main(){

    deque<Person> men;
    vector<Person> women;
    std::tie(men, women) = read_data();
    
    // print_people(women);
    // print_people(men);    

    map<int, int> result = gale_shapley(men, women);

    // Print result: Row i should contain exactly one integer, the index of the man paired with woman i
    for(auto& p : result){
        cout << p.second+1 << endl;
    }

    return 0;
}