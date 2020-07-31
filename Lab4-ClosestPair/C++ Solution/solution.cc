#include "shortest_distance.cc"
#include <iostream>
#include <iomanip>

using std::cin;

point_vector read_create_points();
void free_memory(const point_vector&);

int main(){
    point_vector points = read_create_points();
    double min_distance = shortest_distance(points);
    cout << min_distance << endl;
    cout << std::fixed << std::setprecision(6) << min_distance << endl;

    //free_memory(points);

    return 0;
}

// Parameters and returns are self-explanatory
point_vector read_create_points(){
    int nr_points;
    cin >> nr_points;
    point_vector points;

    int x;
    int y;
    for(int i = 0; i != nr_points; ++i){
        cin >> x >> y;
        points.emplace_back(x, y);
    }

    return points;
}

/*
void free_memory(const point_vector& points) {
    for(auto& p : points) {
        delete p;
    }
}*/