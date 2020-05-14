import sys
from read_create import read_create
from edge import *

""" Solution to lab 6 """

N, M, C, P = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))  # read input

edges, P_edges = read_create(M, P)

source = 0  # source node index
sink = N-1  # sink node index
graph = {}  # dictionary representation of graph
max_flow = 0


def ford_fulkerson(G, s, t):
    """Finds the maximal flow from s to t in G"""
    for node in G.keys():  # reset flow in all edges in G, vill vi göra detta?
        for edge in G[node]:
            edge.set_flow(0)

    # create residual graph, hur? en kopia av G?

    #while # find a path with BFS
    return 0

while max_flow < C:
    """We construct the graph G 'backwards' with respect to P_list until we are above C capacity"""

    new_edge_index = P_edges.pop()
    new_edge = edges[new_edge_index]

    # rimligt?
    if new_edge.destination1 not in graph:
        graph[new_edge.destination1] = [new_edge]
    else:
        graph[new_edge.destination1].append(new_edge)

    if new_edge.destination2 not in graph:
        graph[new_edge.destination2] = [new_edge.reverse()]  # undirected graph
    else:
        graph[new_edge.destination2].append(new_edge.reverse())

    max_flow = ford_fulkerson(graph, source, sink)  # find maximal flow with Ford-Fulkersons algorithm


print(len(P_edges, max_flow))  # len(P_edges) contain how many routes we didn't have to use (#removed edges)


'''
FRÅGOR
- plocka inte bort kant! lägg till kant istället, börja bakifrån (av P)!
-> eftersom vi gör detta kommer s och t ändras? ska vi då ha koll på vad de aktuella s och t är? 
    - nej? s=0, t=N-1?
    
- rimligt att ha en lista med grannar för varje nod i grafen?
- rad 19
- rad 23
- vad används c för på sida 107?
'''
