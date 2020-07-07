#ifndef PERSON_H
#define PERSON_H

#include <iostream>
#include <deque>

using std::deque;
using std::cout;
using std::endl;

struct Person{
    Person(int id, deque<int> p) : id(id), preferences(p) {}
    Person(const Person& other) : id(other.id), preferences(other.preferences) {}  // copy constructor
    int id;
    deque<int> preferences;
    friend std::ostream& operator<<(std::ostream&, const Person&);
    bool operator<(const Person&) const;
};

std::ostream& operator<<(std::ostream& o, const Person& p){
    o << "Person id: " << p.id << " and prefs:";
    for(auto& pref : p.preferences){
        o << " " << pref;
    }
    return o;
}

bool Person::operator<(const Person& other) const{
    return id < other.id;
}

#endif