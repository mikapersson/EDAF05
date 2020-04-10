def make_graph(edges):
    """Create graph with given 'edges'"""
    graph = {}
    for edge in edges:  #edge: [ID, otherID, distance]
        tempID = edge[0]
        tempFriend = edge[1]
        distanceToFriend = edge[2]
        tempEdge = [tempFriend, distanceToFriend]

        if tempID not in graph:
            graph[tempID] = []
        graph[tempID].append(tempEdge)

        otherDirection = [tempID, distanceToFriend]
        if tempFriend not in graph:  #add edge in other direction (undirected graph)
            graph[tempFriend] = []
        graph[tempFriend].append(otherDirection)

    return graph





