def make_graph(edges):
    
    graph = {}
    for edge in edges:
        tempID = edge[0]
        tempFriend = edge[1]
        distanceToFriend = edge[2]
        tempEdge = [tempFriend, distanceToFriend]

        if tempID not in graph:
            newFriend = Friend(tempID)
            newFriend.friends.append(tempEdge)
            graph[tempID] = newFriend
        else:
            graph[tempID].friends.append(tempEdge)

        otherDirection = [tempID, distanceToFriend]
        if tempFriend not in graph:  #add edge in other direction (undirected graph)
            otherFriend = Friend(tempFriend)
            otherFriend.friends.append(otherDirection)
            graph[tempFriend] = otherFriend
        else:
            graph[tempFriend].friends.append(otherDirection)

    return graph





