from Node import Node

class DisjointSets(object):
    """
    Union-find disjoint sets datastructure, see section 3.7 in course book.
    No error handling.
    """

    def __init__(self, vertexList):
        self.nodeCount = 0            #number of elements in the structure
        self.setCount = 0             #number of disjoint sets in the structure  //remove?
        self.vertexList = vertexList  #the vertices in the graph
        self.rootNodes = []           #the root nodes in the disjoint sets datastructure
        self.makeSets(vertexList)     #create the disjoint sets from the vertices

    def makeSets(self, vertexList):
        for v in vertexList:
            self.makeSet(v)

    def makeSet(self, vertex):
        node = Node(0, len(self.rootNodes), None)  #instatiate node to be placed in the dj-structure
        self.rootNodes.append(node)  #O(1)
        self.setCount += 1
        self.nodeCount += 1

    def info(self):
        """
        Print structure information.
        """
        print("UnionFind:\n\tSize = {}\n\tNumber of disjoint sets = {}"
              .format(self.nodeCount, self.setCount))

    def find(self, node):
        """
        Find/return the ID of the representative node for the set in which 'node' is contained.
        (page 81 in the course book)
        """
        currentNode = node
        while currentNode.parentNode is not None:
            currentNode = currentNode.parentNode

        root = currentNode
        currentNode = node

        while currentNode.parentNode is not None:  #path compression
            temp = currentNode.parentNode
            currentNode.parentNode = root
            currentNode = temp

        return root.nodeId

    def sameSet(self, node1ID, node2ID):
        """
        Examine if the nodes 'first' and 'second' belong to the same set,
        return True if so, otherwise False.
        """

        node1 = self.rootNodes[node1ID-1]  #O(1)
        node2 = self.rootNodes[node2ID-1]
        return self.find(node1) == self.find(node2)

    def union(self, node1ID, node2ID):
        """
        Merge the two sets in which first and second belong to.
        """
        index1 = node1ID-1
        index2 = node2ID-1

        node1 = self.rootNodes[index1]
        node2 = self.rootNodes[index2]

        if index1 == index2: return

        root1 = self.rootNodes[self.find(node1)]
        root2 = self.rootNodes[self.find(node2)]

        if root1.height < root2.height:
            root1.parentNode = root2
            root2.height += 1
        elif root2.height < root1.height:
            root2.parentNode = root1
            root1.height += 1
        else:
            root2.parentNode = root1
            root1.height += 1  #ROTEN SKA INKREMENTERAS

        self.setCount -= 1
