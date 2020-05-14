
class Edge:
    """Class describing edge of graph in lab6"""
    def __init__(self, dest1, dest2, cap):
        self.destination1 = dest1
        self.destination2 = dest2
        self.capacity = cap
        self.flow = 0
        self.delta = cap

    def is_full(self):
        return self.flow == self.capacity

    def set_flow(self, new_flow):
        self.flow = new_flow
        self.delta = self.capacity - new_flow

    def increment_flow(self, delta):
        self.flow += delta
        self.delta -= delta

    def print_edge(self):
        output = "Edge: from " + str(self.destination1) + " to " + str(self.destination2) \
                 + " with capacity " + str(self.capacity) + ", flow " + str(self.flow) + " and delta " + str(self.delta)
        print(output)

    def reverse(self):
        """Returns this edge but in the other direction"""
        return Edge(self.destination2, self.destination1, self.capacity)
