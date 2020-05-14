import sys
from edge import Edge


def read_create(nr_edges, P):
    """Read input and create the corresponding edges"""
    edges = [0]*nr_edges
    P_list = [0]*P

    for pos in range(nr_edges):
        dest1, dest2, cap = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
        edges[pos] = Edge(dest1, dest2, cap)

    for pos in range(P):
        P_list[pos] = int(sys.stdin.readline().replace('\n', ''))

    return edges, P_list