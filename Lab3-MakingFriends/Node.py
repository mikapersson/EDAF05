
class Node(object):
    """
    Class representing a node in the disjointsets structure
    for use in Kruskals algorithm.
    """
    def __init__(self, height, nodeId, parentNode):
        self.height = height
        self.nodeId = nodeId
        self.parentNode = parentNode