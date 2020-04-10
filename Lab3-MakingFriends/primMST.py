from heapq import heappush, heappop

def prim(graph):
    """Return the sum of the costs of the edges in the minimum spanning
    tree for the given graph, which must be a mapping from nodes to an
    iterable of (neighbour, edge-cost) pairs.

    Complexity: https://wiki.python.org/moin/TimeComplexity
    """
    total = 0                   # Total cost of edges in tree
    explored = set()            # Set of vertices in tree
    start = next(iter(graph))   # Arbitrary starting vertex
    unexplored = [(0, start)]   # Unexplored edges ordered by cost
    while unexplored:
        cost, closest = heappop(unexplored)  #O(log n)
        if closest not in explored:  #worst case O(n), average O(1)
            explored.add(closest)  #O(1)
            total += cost
            for neighbour, cost in graph[closest].friends:  #problem
                if neighbour not in explored:
                    heappush(unexplored, (cost, neighbour))
    print(total)