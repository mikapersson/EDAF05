import make_graph
import sys
import time
import queue

"""Solution for Wordladders, may be improved.."""

N, Q = list(map(int, sys.stdin.readline().split(' ')))  # reading number of words and queries
words = [0]*N
for i in range(N):  # reading five-letter words
    words[i] = sys.stdin.readline().replace('\n','')

gstime = time.time()  # start stopwatch for graph creation
graph = make_graph.make_graph(words)  # O(n^2)
getime = time.time()  # end stopwatch for graph creation
gtime = getime - gstime  # total time for graph creation


def find_node(word):  # O(n), no error handling
    """Finds the node in the graph corresponding to 'word' (used in the list implementation)"""
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


def BFS(graph, s, t):  # s and t are Node objects
    """BFS algorithm (p.88 in the course book)"""
    if s.word == t.word:
        print(0)
        return
    s.visited = 1
    q = queue.Queue(maxsize=N)
    q.put(s)
    while q.qsize() > 0:
        v = q.get()  # constant
        for adj in v.adj_list:
            if adj.visited == 0:
                adj.visited = 1
                q.put(adj)
                adj.prev = v
                if adj.word == t.word:
                    print(countEdges(adj))  # Could use count attribute instead of traversing backwards to prev
                    return                  # since we don't need to know the path
    print("Impossible")


queries = []
for i in range(Q):  # reading queries
    queries.append(sys.stdin.readline().replace('\n','').split(' '))

astime = time.time()  # start stopwatch for algorithm
for q in queries:     # running algorithm
    # n1 = find_node(q[0])
    # n2 = find_node(q[1])
    # BFS(graph, n1, n2)
    BFS(graph, graph[q[0]], graph[q[1]])

    #RESET GRAPH
    for n in graph.items():  # comment this and we go from 5sec to 0.03sec running time for the algorithm
        n[1].visited = 0     # REMOVE COMMENTS IF TESTING THE PROGRAM
        n[1].prev = 0        #

aetime = time.time()
atime = aetime - astime  # total time for running algorithm
# print("Create graph: {}\nRun algorithm: {}".format(gtime, atime))  #comment when running check_solution.sh
