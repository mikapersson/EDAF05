from queue import Queue
import math

def find_path(G, s, t):  # O(m)
    """Finds path from s to t using BFS"""

    for node in G.values():
        node.visited = 0

    path_exists = None
    path_edges = []
    delta = math.inf  # not sure we keep this

    s.visited = 1
    queue = Queue(maxsize=len(G))
    queue.put(s)
    while queue.qsize() > 0:
        temp_city = queue.get()
        for temp_edge in temp_city.edges:
            if not temp_edge.is_full():
                temp_delta = temp_edge.delta
                if delta > temp_delta:
                    delta = temp_delta
                next_city_index = temp_edge.destination2
                next_city =
            return 0

    delta = 1

    return path_exists, path_edges, delta
