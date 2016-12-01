"""
CSCI-665 Homework 5: Problem 2
This program basically computes the length of the longest path in a given directed
acyclic graph using topological ordering and the dynamic programming, the running
time complexity of the given algorithm is O(M + N).

author: Kapil Dole
author: Chirag Kular
"""
import sys

class Node:
    """
    The given class node is used to store vertex related information.
    """
    __slots__ = 'value', 'edgeList', 'visited', 'longestPath', 'finish'

    def __init__(self, value):
        """
        This is constructor of our class used for initializing, vertex
        related information.

        :param value: Vertex value.
        """
        self.value = value
        self.edgeList = []
        self.visited = False
        self.longestPath = 0
        self.finish = sys.maxsize


def topologicalOrder(vertices, edges, verticesList):
    """
    This method takes vertices and edges of graph as input and
    gives topologically ordered list as output after processing
    it. The time complexity of the algorithm is O(M + N).

    :param vertices: Number of vertices.
    :param edges: Number of edges.
    :param verticesList: List of vertices.
    :return: Topologically ordered list.
    """
    tempFinish = 0
    orderedList = []

    for vertex in range(vertices):
        if not verticesList[vertex].visited:
            # Running DFS for each non visited vertex.
            DFS(verticesList[vertex], orderedList, tempFinish)
    orderedList.reverse()

    return orderedList


def DFS(vertex, orderedList, tempFinish):
    """
    This is helper function used for traversing the vertices
    using DFS and while doing so maintain their finishing order.
    The complexity is O(M + N).

    :param vertex: Start vertex for DFS.
    :param orderedList: Ordered list in vertices finishing order.
    :param tempFinish: Temporary variable for storing finish order.
    :return: None.
    """
    vertex.visited = True

    for neighbour in vertex.edgeList:
        if not neighbour.visited:
            DFS(neighbour, orderedList, tempFinish)

    tempFinish += 1
    vertex.finish = tempFinish
    orderedList.append(vertex)


def longestPath(orderedList):
    """
    This function computes the longest path in the graph using
    dynamic programming. The complexity is O(N).

    :param orderedList: Topologically ordered list.
    :return: Longest path in the graph.
    """
    for vertex in orderedList:
        for neighbour in vertex.edgeList:
            neighbour.longestPath = max(1 + vertex.longestPath, neighbour.longestPath)

    return orderedList[len(orderedList) - 1].longestPath


def main():
    """
    This is main function of our program, which takes input from standard input and
    displays the longest path after processing input vertices and edges.
    :return: None.
    """
    sys.setrecursionlimit(1500)
    vertices, edges = [int(num) for num in input().strip().split()]
    verticesList = []

    for counter in range(vertices):
        verticesList.append(Node(counter))

    # Creating edge list.
    for index in range(edges):
        vertex1, vertex2 = [int(num) for num in input().strip().split()]
        verticesList[vertex1].edgeList.append(verticesList[vertex2])

    orderedList = topologicalOrder(vertices, edges, verticesList)

    print(longestPath(orderedList))


if __name__ == '__main__':
    main()