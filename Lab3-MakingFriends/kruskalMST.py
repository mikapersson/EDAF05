from disjointsets import DisjointSets
from heapq import *
from Node import Node
from time import time

def setup(edges):
    """
    Sort edges in O(nlogn) time according to distance,
    one edge has two nodes, firstNode and secondNode.
    """
    vertices = []
    sortedEdges = []  #priority queue
    for edge in edges:
        distance = edge[2]
        firstNode = edge[0]
        secondNode = edge[1]
        if firstNode not in vertices:
            vertices.append(firstNode)
        if secondNode not in vertices:
            vertices.append(secondNode)
        heappush(sortedEdges, (distance, [firstNode, secondNode]))
    return sortedEdges, vertices

def kruskal(edges):
    """
    Return the sum of the costs of the edges in the minimum spanning
    tree for the given edges.
    """
    print("Starting setup: sorting edges in pq and creating list of vertices")
    sstime = time()
    sortedEdges, vertices = setup(edges)  #O(nlogn)
    estime = time()
    setuptime = estime - sstime
    print("Finished setup in: ", setuptime)
    print("Initializing disjoint sets")
    djstime = time()
    ufset = DisjointSets(vertices)
    djetime = time()
    djtime = djetime - djstime
    print("Finished initialization of dj-set in: ", djtime)
    minWeight = 0

    print("Entering while loop")
    while sortedEdges:
        distance, nodes = heappop(sortedEdges)
        node1 = nodes[0]
        node2 = nodes[1]
        sameSet = ufset.sameSet(node1, node2)
        if not sameSet:
            minWeight += distance
            ufset.union(node1, node2)
    print("Exiting while")

    print(minWeight)