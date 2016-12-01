import sys
import time

from GraphVertexHeap import Graph,Vertex,Heap

def main():
    negativeGraph = Graph()
    noOfVert, noOfEdge = [int(value) for value in input().strip().split()]

    for index in range(noOfEdge):
        startVertex, endVertex, weight = [int(value) for value in input().strip().split()]
        if weight < 0:
            negativeTo = startVertex
            negativeFrom = endVertex
            negativeWeight = weight

        negativeGraph.addEdge(startVertex, endVertex, weight)

    print(CheckNegativeCycle(negativeGraph, negativeFrom, negativeTo, negativeWeight))



def weightcmp(n1, n2):
    """
    Simple comparison function for distance of two vertices
    :param n1: Instance of Node 1
    :param n2: Instance of Node 2
    :return: True if n1 is less than n2
    """
    return n1[0] < n2[0]

def CheckNegativeCycle(graph, startVertex, endVertex, negativeWeight):

    #Inititalize Heap
    H = Heap(weightcmp)
    #Initialize distance to infinity for every vertex
    distance = [sys.maxint for vertex in graph.getVertices()]

    #Initialize distance of starting vertex to zero
    distance[startVertex] = 0

    #Insert the vertex and its distance as a tuple in the Heap
    for v in graph.getVertices():
        H.insert((distance[v],v))

    #Repeat until Haap is not empty
    while not H.isEmpty():
        #Remove the element with smallest distance from the heap
        u = graph.vertList[int(H.pop())]
        #Explore the neighbours of the current vertex
        for v in u.getConnections():
            if distance[v.id] > distance[u.id] + u.getWeight(v):
                distance[v.id] = distance[u.id] + u.getWeight(v)

    #Get the distance of the endVertex from the distance list
    value = distance[endVertex]
    #If the sum of the negative weight and distance of the endVertex is negative, then there is negative cycle
    if value + negativeWeight < 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    main()
