import sys
from readcreatepoints import read_create_points
from math import inf
from point import distance, check_pair

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
    print("{:.6f}".format(closest_dist))


def closest_rec(p_x, p_y, size):
    """
    Recursive function for dividing the set of points.
    """
    if size <= 3:  # base case 1, compute minimum distance of the points (may be compressed)
        base_distance = inf
        base_points = [0]*size
        for index, base_point in enumerate(p_x):
            base_points[index] = base_point

        for p1 in range(size-1):  # loop through base points, no need to loop until the last point
            for p2 in range(p1+1, size):
                temp_distance = distance(base_points[p1], base_points[p2])
                if temp_distance < base_distance:
                    base_distance = temp_distance
        return base_distance

    cut = size//2  # middle index of points lists
    middle_point = p_x[cut]

    left_x = p_x[:cut]  # split p_x in half
    left_y = []  # this is filled below
    right_x = p_x[cut:]
    right_y = []

    left_side = set(left_x)  # for looking up points efficiently
    for point in p_y:  # split p_y in half
        if point in left_side:
            left_y.append(point)
        else:
            right_y.append(point)

    left_distance = closest_rec(left_x, left_y, cut)  # calculate minimum distance on left side
    right_distance = closest_rec(right_x, right_y, size - cut)  # -||- right side
    delta = min(left_distance, right_distance)

    interval_points = []  # points that have an x-coordinate within the distance 'delta' of the 'middle_point'
    # left_interval = set()
    # right_interval = set()
    for y_point in p_y:
        inside_interval = abs(y_point.x - middle_point.x) < delta
        if inside_interval:  # y_point is inside the middle interval of width 2*delta
            interval_points.append(y_point)
            '''
            if y_point in left_side:
                left_interval.add(y_point)
            else:
                right_interval.add(y_point)
            '''

    interval_length = len(interval_points)
    for index1, point1 in enumerate(interval_points):  # brute force, check closest 15 points in y-direction
        last_index = 15 + index1 # index for the last element we are checking the distance to
        if last_index > interval_length:
            last_index = interval_length

        for index2 in range(index1+1, last_index):
            point2 = interval_points[index2]
            closer = distance(point1, point2)
            if closer < delta:
                delta = closer

    return delta


closest_distance(points)  # run algorithm: 1min 8sec
