from queue import Queue
import math


def find_path(G, s, t):  # O(m)
    """Finds path from s to t using BFS"""

    for node in G.values():
        node.visited = False
        node.previous_node = None
        node.previous_edge = None

    path_exists = False

    s.visited = 1
    queue = Queue(maxsize=math.inf)
    queue.put(s)

    # debug_counter = 0
    while queue.qsize() > 0 and not path_exists:  # while there is a potential path from s to t
        temp_city = queue.get()            # the first city in the queue
        temp_city.visited = True
        # print("new city")
        for temp_edge in temp_city.edges:  # examine all edges from temp_city
            if temp_edge.destination1 == temp_city:
                next_city = temp_edge.destination2
            else:
                next_city = temp_edge.destination1

            if not (temp_edge.is_full(next_city) or next_city.visited):  # if the current edge is not filled
                queue.put(next_city)
                next_city.previous_node = temp_city
                next_city.previous_edge = temp_edge

                if next_city == t:  # if we've reach the end station (t)
                    path_exists = True
                    break

    return path_exists
