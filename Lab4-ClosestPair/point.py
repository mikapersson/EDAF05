from math import sqrt


class Point(object):
    """
    Class describing a Point object, which we will use when comparing distances between points.
    """
    def __init__(self, x, y):
        self.x = x  # x coordinate
        self.y = y  # y coordinate


def distance(point1, point2):
    """
    Computes and returns the Euclidean distance between two Points objects.
    """
    return sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


def check_pair(point1, point2, delta):
    """
    Examine if the distance between 'point1' and 'point2' is less than 'delta',
    returns True is so, otherwise False.
    """
    return distance(point1, point2) < delta
