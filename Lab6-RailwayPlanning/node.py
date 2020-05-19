
class Node:
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.visited = False      # 0 if not visited, 1 otherwise
        self.previous_node = None
        self.previous_edge = None
