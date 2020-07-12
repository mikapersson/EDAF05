class Node:
    """Class describing a node (five letter word)"""

    def __init__(self, w, al, v, p):
        self.word = w  #actual word
        self.adj_list = al  #list of nodes that this node has an edge to
        self.visited = v  #0 if not visited, 1 if visited
        self.prev = p  #previous node