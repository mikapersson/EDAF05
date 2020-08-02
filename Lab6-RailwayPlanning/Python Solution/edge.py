
class Edge:
    """Class describing edge of graph in lab6"""
    def __init__(self, dest1, dest2, cap):
        self.destination1 = dest1  # these are node objects
        self.destination2 = dest2
        self.capacity = cap
        self.flow_front = 0
        self.flow_back = 0

    def is_full(self, node):
        """Check if flow=capacity towards node 'node'"""
        if node == self.destination2:
            return self.capacity == self.flow_front
        else:
            return self.capacity == self.flow_back

    def get_capacity(self, node):
        """Get capacity towards node 'node'"""
        if node == self.destination2:
            return self.capacity - self.flow_front
        else:
            return self.capacity - self.flow_back

    def update_flow(self, node, delta):
        """Increase flow with 'delta' towards node 'node'"""
        if node == self.destination2:
            self.flow_front += delta
            self.flow_back -= delta
        else:
            self.flow_back += delta
            self.flow_front -= delta

    def print_edge(self):
        output = "Edge: from " + str(self.destination1) + " to " + str(self.destination2) \
                 + " with capacity " + str(self.capacity) + ", flow_front " + str(self.flow_front) \
                 + " and flow_back " + str(self.flow_back)
        print(output)
