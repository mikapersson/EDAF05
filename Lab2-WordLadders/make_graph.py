import Node


def make_nodes(words):
    """Returns a list of nodes corresponding to the words in 'words'-list"""
    #nodes = []  #list implementation
    nodes = {}  #dictionary implementation, word (key): Node-object (value)
    for w in words:
        #nodes.append(Node.Node(w, [], 0, 0))
        nodes[w] = Node.Node(w, [], 0, 0)
    return nodes

def edgeExists(w1, w2):
    """Check if there is an edge from w1 to w2"""
    exist = []
    for char in w1[1:]:
        if char in w2:
            exist.append(True)
            w2 = w2.replace(char,'',1)
        else:
            exist.append(False)

    return all(exist)

def make_graph(words):
    """Creating graph from 'words', a list of five letter words (dictionary representation)"""
    graph = make_nodes(words)
    for current in graph.items():
        for temp in graph.items():
            if edgeExists(current[0], temp[0]) and current != temp:
                #current.adj_list.append(temp)
                current[1].adj_list.append(temp[1])
    return graph




