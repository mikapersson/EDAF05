import sys
from point import Point


def read_create_points(nr_points):
    points = [0]*nr_points  # list containing Point objects
    for i in range(nr_points):
        x, y = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
        new_point = Point(x, y)
        points[i] = new_point

    return points
