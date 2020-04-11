import sys
from readcreatepoints import read_create_points

"""Solution for Closest Pair lab"""

nr_points = int(sys.stdin.readline().replace('\n', ''))  # number of points to compare
points = read_create_points(nr_points)  # read and create list of Point objects
points.sort(key=lambda point: point.x)  # sort points according to x-coordinate


def closest_distance(point_list):
    """
    Finds and returns the shortest distance between two of the input points.
    (p.40 in course book)
    """
    middle = len(point_list)//2
    left_points = point_list[:middle]
    right_points = point_list[middle:]
    closest_dist = closest_rec(left_points, right_points, len(point_list))
    print(closest_dist)


def closest_rec(left, right, size):
    """
    Recursive function for dividing the set of points.
    """

    return 0


closest_distance(points)  # run algorithm
