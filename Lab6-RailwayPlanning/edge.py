
class Edge:
    """Class describing edge of graph in lab6"""
    def __init__(self, dest1, dest2, cap):
        self.destination1 = dest1  # these are node objects
        self.destination2 = dest2
        self.capacity = cap
        self.flow_front = 0
        self.flow_back = 0

    def is_full(self, node):
        if node == self.destination2:
            return self.capacity == self.flow_front
        else:
            return self.capacity == self.flow_back

    def get_capacity(self, node):
        if node == self.destination2:
            return self.capacity - self.flow_front + self.flow_back
        else:
            return self.capacity - self.flow_back + self.flow_front

    def update_flow(self, node, delta):
        if node == self.destination2:
            if self.flow_back >= delta:
                self.flow_back -= delta
            else:
                self.flow_front += delta - self.flow_back
                self.flow_back = 0

        else:
            if self.flow_front >= delta:
                self.flow_front -= delta
            else:
                self.flow_back += delta - self.flow_front
                self.flow_front = 0

    def print_edge(self):
        output = "Edge: from " + str(self.destination1) + " to " + str(self.destination2) \
                 + " with capacity " + str(self.capacity) + ", flow_front " + str(self.flow_front) \
                 + ", front_back " + str(self.flow_back) + " and delta " + str(self.delta)
        print(output)
