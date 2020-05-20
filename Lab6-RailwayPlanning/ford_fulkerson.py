from copy import deepcopy
from find_path import find_path
from math import inf


def ford_fulkerson(G, start_index, end_index):
    """Finds the maximal flow from s to t in G"""
    # print("Entered FF")
    tot_flow = 0

    if start_index in G:  # if we've added the source node to the graph
        source_node = G[start_index]
    else:
        return 0

    if end_index in G:  # if we've added the sink node to the graph
        sink_node = G[end_index]
    else:
        return 0

    # debug_counter = 0
    path_exists = find_path(G, source_node, sink_node)  # here 'temp_point' is 't'
    while path_exists:  # while there is a path that isn't clogged up
        # print(debug_counter)
        delta = inf
        temp_node = sink_node

        while temp_node != source_node:  # find minimal delta
            delta = min(delta, temp_node.previous_edge.get_capacity(temp_node))
            temp_node = temp_node.previous_node

        tot_flow += delta
        temp_node = sink_node
        while temp_node != source_node:  # update flow along the found path
            temp_node.previous_edge.update_flow(temp_node, delta)
            temp_node = temp_node.previous_node

        path_exists = find_path(G, source_node, sink_node)

        # debug_counter += 1

    return tot_flow
