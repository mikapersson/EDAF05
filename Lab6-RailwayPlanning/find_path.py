from queue import Queue
import math


def find_path(G, s, t):  # O(m)
    """Finds path from s to t using BFS"""

    for node in G.values():
        node.visited = 0

    path_exists = False
    path_edges = []
    delta = math.inf

    s.visited = 1
    queue = Queue(maxsize=len(G))
    queue.put(s)

    while queue.qsize() > 0:               # while there is a potential path from s to t
        temp_city = queue.get()            # the first city in the queue
        temp_city.visited = 1

        for temp_edge in temp_city.edges:  # examine all edges from temp_city
            next_city_index = temp_edge.destination2  # find the next city
            next_city = G[next_city_index]
            is_visited = next_city.visited == 1

            if not (temp_edge.is_full() or is_visited):    # if the current edge is not filled
                temp_delta = temp_edge.delta
                if delta > temp_delta:     # in order to find the least delta
                    delta = temp_delta

                queue.put(next_city)

                next_city.previous = temp_city
                path_edges.append(temp_edge)

                if next_city == t:  # if we've reach the end station (t)
                    path_exists = True
                    break

    return path_exists, path_edges, delta
