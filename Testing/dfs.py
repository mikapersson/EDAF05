import sys
from node import Node
from edge import Edge


# SETUP
N, M = list(map(int, sys.stdin.readline().replace('\n', '').split()))

graph = {}
nodes = [Node(i) for i in range(N)]
for index, node in enumerate(nodes):
    graph[index] = node

edges = [0]*M

for row in range(M):
    node1, node2 = list(map(int, sys.stdin.readline().replace('\n', ' ').split()))
    temp_edge = Edge(nodes[node1], nodes[node2])
    nodes[node1].succ.append(temp_edge)


# SOLUTION
def dfs(v, depth):
    global counter
    v.shortest = depth
    v.dfsnum = counter
    v.visited = True
    counter += 1
    depth += 1

    new_depth = depth
    for edge in v.succ:
        next_node = edge.node2
        if not next_node.visited:
            new_depth = dfs(next_node, depth)

    deepest = new_depth if new_depth > depth else depth
    return deepest


def print_graph_indices(G):
    for item in G.values():
        item.print_node()


def print_shortest_paths(G):
    print("Shortest paths in the DFS-tree (OBS), how do we do it for the graph?")
    for item in G.values():
        item.print_shortest()


counter = 0
start_node = nodes[0]
dep = dfs(start_node, 0)

# print("Depth is {}".format(dep))
print_shortest_paths(graph)












