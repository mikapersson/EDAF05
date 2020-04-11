import sys
from readcreatepoints import read_create_points

"""Solution for Closest Pair lab"""

nr_points = int(sys.stdin.readline().replace('\n', ''))
points = read_create_points(nr_points)

print(nr_points)
