#include <vector>
#include <map>
#include "person.h"
#include <deque>

using std::vector;
using std::map;
using std::deque;

/**
 * Gale-Shapley algorithm (p.117 in course book)
 * 
 * @param men   deque with (Person objects) men to be paired
 * @param women vector with (-||-) women to be paired
 * @return map with pair-containers corresponding to each man-woman pair
 */
map<int, int> gale_shapley(deque<Person>& men, vector<Person>& women){
    deque<Person> p(men);
    map<int, int> pairs;

    while(p.size() > 0){
        Person man(p[0]);
        int man_id(man.id);   // take out the first element of p (Person object)
        p.pop_front();        // delete first element in men-deque

        int woman_id(man.preferences[0]);  // the woman 'man' prefers the most and hasn't proposed to yet
        man.preferences.pop_front();

        if(pairs.find(woman_id) == pairs.end()){  // if 'woman' doesn't have a partner
            pairs[woman_id] = man_id;
        } else {                                  // determine if 'woman' prefers 'man' over her current partner
            Person current(men[pairs[woman_id]]); 
            if(women[woman_id].preferences[man_id] < women[woman_id].preferences[current.id]){
                pairs.erase(woman_id);
                pairs[woman_id] = man_id;
                p.push_back(current);
            } else {
                p.push_back(man);
            }
        }
    }
    return pairs;
}