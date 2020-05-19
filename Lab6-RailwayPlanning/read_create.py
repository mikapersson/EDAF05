import sys
from node import Node
from edge import Edge


def read_create(nr_nodes, nr_edges, P):
    """Read input and create the corresponding edges"""

    nodes = [0]*nr_nodes
    for n in range(nr_nodes):  # create and add nodes to nodes list
        new_node = Node(n)
        nodes[n] = new_node

    edges = [0]*nr_edges
    P_list = [0]*P

    for pos in range(nr_edges):
        dest1, dest2, cap = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))
        node1 = nodes[dest1]
        node2 = nodes[dest2]
        edges[pos] = Edge(node1, node2, cap)

    for pos in range(P):
        P_list[pos] = int(sys.stdin.readline().replace('\n', ''))

    return nodes, edges, P_list