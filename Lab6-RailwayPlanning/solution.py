import sys
from read_create import read_create
from node import Node
from ford_fulkerson import ford_fulkerson

""" Solution to lab 6 """
sys.setrecursionlimit(10**9)
# SETUP
N, M, C, P = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))  # read input
nodes, edges, P_edges = read_create(N, M, P)

source = 0  # source node index
sink = N - 1  # sink node index
graph = {}  # dictionary representation of graph

# SOLUTION
for index, edge in enumerate(edges):  # create graph
    if index not in P_edges:
        from_node = edge.destination1
        from_node_index = from_node.index
        to_node = edge.destination2
        to_node_index = to_node.index

        if from_node_index not in graph:
            from_node.edges.append(edge)
            graph[from_node_index] = from_node
        else:
            graph[from_node_index].edges.append(edge)

        if to_node_index not in graph:
            to_node.edges.append(edge)
            graph[to_node_index] = to_node  # undirected graph
        else:
            graph[to_node_index].edges.append(edge)

# iteration = 0
max_flow = ford_fulkerson(graph, source, sink)  # current max-flow in 'graph'
while max_flow < C:                             # add an edge in 'P_edges' at a time
    # iteration += 1
    new_edge_index = P_edges.pop()  # O(1)
    new_edge = edges[new_edge_index]

    from_node = new_edge.destination1
    from_node_index = from_node.index
    to_node = new_edge.destination2
    to_node_index = to_node.index

    if from_node_index not in graph:
        from_node.edges.append(new_edge)
        graph[from_node_index] = from_node
    else:
        graph[from_node_index].edges.append(new_edge)

    if to_node_index not in graph:
        to_node.edges.append(new_edge)
        graph[to_node_index] = to_node  # undirected graph
    else:
        graph[to_node_index].edges.append(new_edge)

    max_flow += ford_fulkerson(graph, source, sink)  # find maximal flow with Ford-Fulkersons algorithm
    # print("iteration", iteration)
    # print(max_flow)


print(len(P_edges), max_flow)  # len(P_edges) contain how many routes we didn't have to use (#removed edges)

