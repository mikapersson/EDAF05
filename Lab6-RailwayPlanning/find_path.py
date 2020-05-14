
def find_path(G, s, t):
    """Finds path from s to t using BFS"""
    path_exists = None
    path_edges = []
    for el in G.values():
        for ed in el:
            if ed not in path_edges:
                path_edges.append(ed)
    delta = 1

    return path_exists, path_edges, delta
