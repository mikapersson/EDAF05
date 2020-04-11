import sys
from readcreatepoints import read_create_points

"""Solution for Closest Pair lab"""

nr_points = int(sys.stdin.readline().replace('\n', ''))  # number of points to compare
points = read_create_points(nr_points)  # read and create list of Point objects


def closest_distance(point_list):
    """
    Finds and returns the shortest distance between two of the input points.
    (p.40 in course book)
    """
    points_x = point_list
    points_y = point_list.copy()
    points_x.sort(key=lambda point: point.x)  # sort points according to x-coordinate
    points_y.sort(key=lambda point: point.y)  # sort points according to y-coordinate
    closest_dist = closest_rec(points_x, points_y, len(point_list))
    print(closest_dist)


def closest_rec(p_x, p_y, size):
    """
    Recursive function for dividing the set of points.
    """
    # BASE CASE, WHEN DO WE DO THIS?

    cut = size//2  # middle index of points lists
    middle_point = p_x[cut]

    left_x = p_x[:cut]  # split p_x in half
    left_y = [0]*cut  # this is filled below
    right_x = p_x[cut:]
    right_y = [0]*(size-cut)

    left_side = set(left_x)  # for looking up points efficiently
    for index, point in enumerate(p_y):  # split p_y in half
        if point in left_side:
            left_y[index] = point
        else:
            right_y[index] = point

    left_distance = closest_rec(left_x, left_y, cut)  # calculate minimum distance on left side
    right_distance = closest_rec(right_x, right_y, size - cut)  # -||- right side
    delta = min(left_distance, right_distance)

    return 0


closest_distance(points)  # run algorithm
