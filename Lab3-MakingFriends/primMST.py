from heapq import heappush, heappop

def prim(graph):
    """
    Return the sum of the costs of the edges in the minimum spanning
    tree for the given graph (dictionary), which must be a mapping from nodes to an
    iterable of (friendID, distance)-pairs (integer pairs).

    Complexity: https://wiki.python.org/moin/TimeComplexity
    """
    total = 0                   # Total cost of edges in MST
    explored = set()            # Set of vertices in MST
    start = next(iter(graph))   # Arbitrary starting vertex
    unexplored = [(0, start)]   # Unexplored edges ordered by cost (priority queue / heap)
    while unexplored:           #we want O(mlogn), m-nr edges, m-nr nodes/friends
        cost, closest = heappop(unexplored)  #pop: O(log n)
        if closest not in explored:          #check set: O(1)
            explored.add(closest)            #add: O(1)
            total += cost
            for neighbour, cost in graph[closest]:
                if neighbour not in explored:
                    heappush(unexplored, (cost, neighbour))  #O(log n)
    print(total)