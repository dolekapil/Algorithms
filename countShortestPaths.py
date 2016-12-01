"""
CSCI-665 Homework 5: Problem 1
This program basically computes the number of shortest paths from given vertex1
to vertex2 in given undirected graph. We have used modified breadth first search
for computing the number of shortest paths. The running time complexity of our
algorithm is O(M + N).

author: Kapil Dole
author: Chirag Kular
"""

class Node:
    """
    The given class node is used to store vertex related information.
    """
    __slots__ = 'value', 'edgeList', 'visited'

    def __init__(self, value):
        """
        This is constructor of our class used for initializing, vertex
        related information.

        :param value: Vertex value.
        """
        self.value = value
        self.edgeList = []
        self.visited = False


def countShortestPath(start, destination, verticesList):
    """
    This method basically counts number of shortest path from
    source to destination using BFS, having complexity of
    O(M + N).

    :param start: Starting vertex.
    :param destination: Destination vertex.
    :param verticesList: List of vertices objects.
    :return: Shortest path count.
    """
    # when start is same as destination, return 1.
    if start == destination:
        return 1

    found = False
    countShortest = 0
    currentQueue = [start]
    nextQueue = []
    intermediateQueue = []

    # continue doing modified BFS, till either all of edges are
    # covered or the destination is found.
    while not found and currentQueue:
        currentVert = currentQueue.pop(0)
        for vertex in verticesList[currentVert].edgeList:
            # if vertex is not visited before, then add it in next
            # queue.
            if not verticesList[vertex].visited:
                nextQueue.append(vertex)

        intermediateQueue.append(currentVert)

        # When we found out the destination vertex, stop searching
        # and increment the counter.
        if currentVert == destination:
            found = True
            countShortest += 1
            break

        # When the current queue is empty, then add the contents of
        # next queue into current and reset the next queue.
        if not currentQueue:
            currentQueue = nextQueue
            nextQueue = []
            for vertex in intermediateQueue:
                verticesList[vertex].visited = True
            intermediateQueue = []

    # When the destination is found then count all occurrence of
    # destination in the current queue and return the count.
    if found:
        for value in currentQueue:
            if value == destination:
                countShortest += 1

    return countShortest


def main():
    """
    This is main function of our program, which takes input from standard input and
    displays the count after processing input vertices and edges.
    :return: None.
    """
    vertices, edges = [int(num) for num in input().strip().split()]
    start, destination = [int(num) for num in input().strip().split()]

    verticesList = []

    for counter in range(vertices):
        verticesList.append(Node(counter))

    # Building edge list.
    for index in range(edges):
        vertex1, vertex2 = [int(num) for num in input().strip().split()]
        verticesList[vertex1].edgeList.append(vertex2)
        verticesList[vertex2].edgeList.append(vertex1)

    print(countShortestPath(start, destination, verticesList))


if __name__ == '__main__':
    main()