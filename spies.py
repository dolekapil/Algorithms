
import sys
class Node:

    __slots__ = 'value', 'edgeList', 'parent', 'reliable', 'minCost'

    def __init__(self, value, reliable=True):
        self.value = value
        self.edgeList = []
        self.parent = None
        self.reliable = reliable
        self.minCost = sys.maxsize

def findMinCost(vertices, edges, verticesList, adjMatrix):
    for counter in range(vertices):
        if verticesList[counter].reliable:
            start = counter
            break

    notDoneList = [index for index in range(vertices)]

    verticesList[start].minCost = 0
    notDoneList.remove(start)
    update(start, verticesList, adjMatrix, notDoneList)

    for index in range(1, vertices):
        vertex = findMinCost_helper(vertices, verticesList, notDoneList)
        update(vertex, verticesList, adjMatrix, notDoneList)

    totalMinCost = 0
    for vertex in range(vertices):
        totalMinCost += verticesList[vertex].minCost


    return totalMinCost if totalMinCost < sys.maxsize else 'NONE'

def findMinCost_helper(vertices, verticesList, notDoneList):
    minCost = sys.maxsize
    for counter in range(vertices):
        if verticesList[counter].minCost < minCost and counter in notDoneList:
            if verticesList[counter].reliable:
                minCost = verticesList[counter].minCost
                vertex = counter

    if verticesList[vertex].parent in notDoneList:
        notDoneList.remove(verticesList[vertex].parent)

    return vertex


def update(vertex, verticesList, adjMatrix, notDoneList):
    for neighbour in verticesList[vertex].edgeList:
        if verticesList[neighbour].minCost > adjMatrix[vertex][neighbour] and neighbour in notDoneList:
            verticesList[neighbour].minCost = adjMatrix[vertex][neighbour]
            verticesList[neighbour].parent = verticesList[vertex].value


def main():
    """
    This is main function of our program .
    :return: None.
    """
    vertices, edges = [int(num) for num in input().strip().split()]
    unreliable = int(input().strip())
    unreliableList = [int(value) for value in input().strip().split()]

    verticesList = dict()
    for counter in range(vertices):
        if counter not in unreliableList:
            verticesList[counter] = Node(counter)
        else:
            verticesList[counter] = Node(counter, False)

    adjMatrix = [[sys.maxsize for _ in range(vertices)] for _ in range(vertices)]

    for index in range(edges):
        vertex1, vertex2, vertex3 = [int(num) for num in input().strip().split()]
        if vertex2 not in verticesList[vertex1].edgeList and vertex2 not in unreliableList:
            verticesList[vertex1].edgeList.append(vertex2)
        if vertex1 not in verticesList[vertex2].edgeList and vertex1 not in unreliableList:
            verticesList[vertex2].edgeList.append(vertex1)
        if adjMatrix[vertex1][vertex2] != sys.maxsize and vertex3 < adjMatrix[vertex1][vertex2]:
            adjMatrix[vertex1][vertex2] = vertex3
            adjMatrix[vertex2][vertex1] = vertex3
        elif adjMatrix[vertex1][vertex2] == sys.maxsize:
            adjMatrix[vertex1][vertex2] = vertex3
            adjMatrix[vertex2][vertex1] = vertex3

    print(findMinCost(vertices, edges, verticesList, adjMatrix))
if __name__ == '__main__':
    main()