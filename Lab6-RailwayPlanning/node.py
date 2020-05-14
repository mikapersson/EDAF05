
class Node:
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.visited = 0      # 0 if not visited, 1 otherwise WILL WE USE THIS??
        self.previous = None  # previous node (used when finding path)
