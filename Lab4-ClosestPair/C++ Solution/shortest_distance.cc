#include <vector>
#include <algorithm>
#include <utility>
#include <iostream>
#include <limits>  // std::numeric_limits<float>::max
#include <math.h>  // sqrt, pow
#include <set>

using std::vector;
using std::pair;
using std::cout;
using std::endl;

typedef pair<int, int> point;
typedef vector<point> point_vector;

void print_points(const point_vector&);
double distance(const point&, const point&);

double shortest_distance(const point_vector& points) {
    point_vector points_x(points.begin(), points.end());  // points sorted according to the x-coordinate
    point_vector points_y(points.begin(), points.end());  // -||- y-coordinate
    
    // Sort points according to x- and y-coordinates
    std::sort(points_x.begin(), points_x.end(), [](const point p1, const point p2){
        return p1.first < p2.first;
    });
    std::sort(points_y.begin(), points_y.end(), [](const point p1, const point p2){
        return p1.second < p2.second;
    });

    double min_distance = shortest_distance_rec(points_x, points_y, points.size());
    return min_distance;
}

double shortest_distance_rec(point_vector& p_x, point_vector& p_y, int size) {
    if(size <= 3){  // base case 
        double base_distance = std::numeric_limits<double>::max();
        point_vector base_points;
        for(int i = 0; i != size; ++i) {
            base_points.push_back(p_x[i]);
        }

        for(int p1 = 0; p1 != size-1; ++p1){
            for(int p2 = p1+1; p2 != size; ++p2) {
                double temp_distance = distance(base_points[p1], base_points[p2]);
                if(temp_distance < base_distance) 
                    base_distance = temp_distance;
            }
        }
        return base_distance;
    }

    int middle_index = size/2;  // index for the middle point in point_vectors
    point middle_point = p_x[middle_index];
    point_vector left_x(p_x.begin(), p_x.begin() + middle_index);  // split p_x in half
    point_vector left_y;  // filled out below
    point_vector right_x(p_x.begin() + middle_index, p_x.end());
    point_vector right_y;

    set<point> 
}

// Used for verifying that the point_vectors are correct
void print_points(const point_vector& points) {
    for(const auto& p : points){
        cout << p.first << " : " << p.second << endl;
    }
}

double distance(const point& p1, const point& p2) {
    return sqrt(pow(p1.first - p2.first, 2) + pow(p1.second - p2.second, 2));
}