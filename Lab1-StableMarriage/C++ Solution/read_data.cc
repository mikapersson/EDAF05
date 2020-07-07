#include "person.h"
#include <utility>    // std::pair
#include <set>
#include <algorithm>  // std::sort;
#include <vector>

using std::cin;
using std::pair;
using std::set;
using std::sort;
using std::vector;

/**
 * Read data from files through stdin (because of the check_solution.sh file)
 * 
 * @return deque containing men (Person objects) sorted after Person.id
 * @return vector containing women (-||-) -||-
 */
pair<deque<Person>, vector<Person>> read_data(){
    int nr_pairs;  
    cin >> nr_pairs;  // Read number of pairs

    deque<Person> men;
    vector<Person> women;

    // Read and fill the vectors 'men' and 'women'
    int temp_id;     //temporary id
    cin >> temp_id;
    --temp_id;       // note that we decrement every input to avoid indexing problems
    set<int> ids;    // in order to determine if it's a woman or man (woman appear first)
    int temp_pref;   // temporary preference number
    int counter{1};  // in order to determine if we've finished one person
    const int nr_inputs{2*nr_pairs*(nr_pairs+1)};
    deque<int> temp_prefs;
    
    for(int i = 1; i != nr_inputs; ++i){
        if(counter%(nr_pairs+1) == 0){  // if we are reading for a new person

            if(ids.find(temp_id) == ids.end()){  // if it's a woman
                women.push_back(Person(temp_id, temp_prefs));
                ids.insert(temp_id);
            } else {
                men.push_back(Person(temp_id, temp_prefs));
            }
            temp_prefs.clear();
            cin >> temp_id;
            --temp_id;
        } else {
            cin >> temp_pref;
            --temp_pref;
            temp_prefs.push_back(temp_pref);
        }
        ++counter;
    }
    men.push_back(Person(temp_id, temp_prefs));  // adding the last man (not covered by the last iteration above)

    // Invert preference list for women
    for(auto& woman : women){
        deque<int> inverted_pref(nr_pairs, 0);
        for(deque<int>::size_type i = 0; i != woman.preferences.size(); ++i){
            inverted_pref[woman.preferences[i]] = i;
        }
        woman.preferences = inverted_pref;
    }

    // Sort lists according to id (implement 'operator<' for 'Person')
    std::sort(women.begin(), women.end());
    std::sort(men.begin(), men.end());

    return std::make_pair(men, women);
}


