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
double shortest_distance_rec(point_vector&, point_vector&, int);

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
    // Base case
    if(size <= 3){  
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

    // Split point_vectors in half according to the x-coordinate
    int middle_index = size/2;  // index for the middle point in point_vectors
    point middle_point = p_x[middle_index];
    point_vector left_x(p_x.begin(), p_x.begin() + middle_index);  // split p_x in half
    point_vector left_y;  // filled out below
    point_vector right_x(p_x.begin() + middle_index, p_x.end());
    point_vector right_y;

    std::set<point> left_side(left_x.begin(), left_x.end());  // for efficient point-look-up
    for(const auto& p : p_y) {
        if(left_side.count(p) == 1)
            left_y.push_back(p);
        else right_y.push_back(p);
    }

    double left_distance = shortest_distance_rec(left_x, left_y, middle_index);
    double right_distance = shortest_distance_rec(right_x, right_y, size - middle_index);
    double delta = std::min(left_distance, right_distance);

    // Find points which are within a distance 'delta' of 'middle_point' (x-coordinate)
    point_vector interval_points;
    for(const auto& p : p_y) {
        bool inside_interval = std::abs(p.first - middle_point.first) < delta;
        if(inside_interval)
            interval_points.push_back(p);
    }

    // Brute force: check 15 closest points in y-direction
    auto interval_length = interval_points.size();
    for(point_vector::size_type index1 = 0; index1 != interval_length; ++index1) {
        point point1 = interval_points[index1];
        auto last_index = 15 + index1;
        if(last_index > interval_length)
            last_index = interval_length;

        for(auto index2 = index1+1; index2 != last_index; ++index2){
            point point2 = interval_points[index2];
            double closer = distance(point1, point2);
            if(closer < delta)
                delta = closer;
        }
    }

    return delta;
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