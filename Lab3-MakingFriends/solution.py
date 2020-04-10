import sys
from make_graph import *
from kruskalMST import *
from primMST import *
from time import time

"""Solution for making friends lab"""

#print("Solving problem...")
prims = False  #run Prim's algorithm if True, otherwise Kruskal's algorithm

rstime = time()
N, M = list(map(int, sys.stdin.readline().split(' ')))  #read number of people N and pairs M
edges = [0]*M  #rows containing edge descriptions
for i in range(M):
    descriptionString = sys.stdin.readline().replace('\n', '')
    descriptionList = descriptionString.split(' ')
    edges[i] = list(map(int, descriptionList))  #transforming values from chars to ints

if prims:
    graph = make_graph(edges)  #dictionary representation (int : edges)

retime = time()
readTime = retime - rstime
#print("Time for reading data: ", readTime)
#RUN ALGORITHM
astime = time()
if prims:
    prim(graph)
else:
    #print("Entering Kruskal")
    kruskal(edges)
    #print("Exiting Kruskal")
aetime = time()
algTime = aetime - astime
#print("Total time for reading and creating graph: {}\nTotal time for running algorithm: {}".format(readTime, algTime))






