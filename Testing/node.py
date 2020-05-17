
class Node:

    def __init__(self, index):
        self.index = index
        self.dfsnum = 0
        self.visited = False
        self.succ = []  # list of edges to successors
        self.shortest = 0

    def print_node(self):
        print("Node with index {} and dfs {} and successors:".format(self.index, self.dfsnum))
        for succ in self.succ:
            print("\t{}".format(succ.node2.index))
        print()

    def print_shortest(self):
        print("Node with index {} has shortest path from root {}".format(self.index, self.shortest))

