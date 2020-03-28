import make_graph
import sys
import time

"""Solution for Wordladders, may be improved.."""

N, Q = list(map(int, sys.stdin.readline().split(' ')))  #reading number of words and queries
words = []
for i in range(N):  #reading five-letter words
    words.append(sys.stdin.readline().replace('\n',''))

gstime = time.time()  #start stopwatch for graph creation
graph = make_graph.make_graph(words)  #O(n^2)
getime = time.time()  #end stopwatch for graph creation
gtime = getime - gstime  #total time for graph creation

def find_node(word):  #O(n), no error handling
    """Finds the node in the graph corresponding to 'word'"""
    for n in graph:
        if word == n.word:
            return n

def countEdges(node):
    """Counts how many edges the path from 'node' to it's origin has"""
    count = 0
    while node.prev != 0:
        node = node.prev
        count += 1
    return count

def BFS(graph, s, t):
    """BFS algorithm (p.88 in the course book)"""
    if s.word == t.word:
        print(0)
        return
    for n in graph:
        n.visited = 0
        n.prev = 0
    s.visited = 1
    q = [s]
    while len(q) > 0:
        v = q.pop(0)
        for adj in v.adj_list:
            if adj.visited == 0:
                adj.visited = 1
                q.append(adj)
                adj.prev = v
                if adj.word == t.word:
                    print(countEdges(adj))
                    return
    print("Impossible")

queries = []
for i in range(Q):  #reading queries
    queries.append(sys.stdin.readline().replace('\n','').split(' '))

astime = time.time()  #start stopwatch for algorithm
for q in queries:  #running algorithm
    n1 = find_node(q[0])
    n2 = find_node(q[1])
    BFS(graph, n1, n2)
aetime = time.time()
atime = aetime - astime  #total time for running algorithm
print("Create graph: {}\nRun algorithm: {}".format(gtime, atime))  #comment when running check_solution.sh