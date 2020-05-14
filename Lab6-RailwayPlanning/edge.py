
class Edge:
    """Class describing edge of graph in lab6"""
    def __init__(self, dest1, dest2, cap):
        self.destionation1 = dest1
        self.destionation2 = dest2
        self.capacity = cap
        self.flow = 0

    def is_full(self):
        return self.flow == self.capacity

    def delta(self):
        return self.capacity - self.flow

    def set_flow(self, new_flow):
        self.flow = new_flow

    def increment_flow(self, delta):
        self.flow += delta

    def print_edge(self):
        output = "Edge: from " + str(self.destionation1) + " to " + str(self.destionation2) \
                 + " with capacity " + str(self.capacity) + " and flow " + str(self.flow)
        print(output)

    def reverse(self):
        """Returns this edge but in the other direction"""
        return Edge(self.destionation2, self.destionation1, self.capacity)
