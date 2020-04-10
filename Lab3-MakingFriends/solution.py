import sys
from make_graph import *
from kruskal import *
from primMST import *

"""Solution for making friends lab"""

prims = True  #run Prim's algorithm if True, otherwise Kruskal's algorithm

N, M = list(map(int, sys.stdin.readline().split(' ')))  #read number of people N and pairs M
edges = [0]*M  #rows containing edge descriptions
for i in range(M):
    descriptionString = sys.stdin.readline().replace('\n', '')
    descriptionList = descriptionString.split(' ')
    edges[i] = list(map(int, descriptionList))  #transforming values from chars to ints

graph = make_graph(edges)  #dictionary representation (int : edges)

#RUN ALGORITHM
if prims:
    prim(graph)
else:
    kruskal(graph)






