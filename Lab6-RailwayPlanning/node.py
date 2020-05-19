
class Node:
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.visited = False
        self.previous_node = None
        self.previous_edge = None
