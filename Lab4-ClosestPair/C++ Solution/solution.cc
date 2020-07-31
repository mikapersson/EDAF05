#include "shortest_distance.cc"
#include <iostream>
#include <iomanip>

point_vector read_create_points();
void free_memory(const point_vector&);

int main(){
    point_vector points = read_create_points();
    double min_distance = shortest_distance(points);
    cout << std::fixed << std::setprecision(6) << min_distance << endl;

    return 0;
}