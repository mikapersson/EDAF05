import sys
from readcreatepoints import read_create_points
from math import inf
from point import distance


nr_points = int(sys.stdin.readline().replace('\n', ''))
points = read_create_points(nr_points)

min_distance = inf

# O(n^2) solution
for pos1 in range(len(points)):
    point1 = points[pos1]
    for pos2 in range(pos1+1, len(points)):
        point2 = points[pos2]
        temp_distance = distance(point1, point2)
        if temp_distance < min_distance:
            min_distance = temp_distance

print("{:.6f}".format(min_distance))  # 
