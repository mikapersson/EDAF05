from unionfind import UnionFind
from heapq import *

def sortEdges(edges):
    """Sort edges in O(nlogn) time according to distance, one edge has two nodes, firstNode and secondNode"""
    sortedEdges = []  #priority queue
    for edge in edges:
        distance = edge[2]
        firstNode = edge[0]
        secondNode = edge[1]
        heappush(sortedEdges, (distance, [firstNode, secondNode]))

    return sortedEdges

def kruskal(edges):
    sortedEdges = sortEdges(edges)
    #lägg alla noder i ett set
    #ha koll på hur många 'barn' en nod har under sig
    print(0)