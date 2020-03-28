import Node


def make_nodes(words):
    """Returns a list of nodes corresponding to the words in 'words'-list"""
    nodes = []
    for w in words:
        nodes.append(Node.Node(w, [], 0, 0))
    return nodes

def condition(node1, node2):
    """Check if there is an edge from node1 to node2"""
    exist = []
    w2 = node2.word
    for char in node1.word[1:]:
        if char in w2:
            exist.append(True)
            w2 = w2.replace(char,'',1)
        else:
            exist.append(False)

    return all(exist)

def make_graph(words):
    """Creating graph from 'words', a list of five letter words"""
    graph = make_nodes(words)
    for current in graph:
        for temp in graph:  #a node has an arc to itself
            if condition(current, temp) and current != temp:
                current.adj_list.append(temp)
    return graph




