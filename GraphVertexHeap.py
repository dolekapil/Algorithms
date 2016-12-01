"""
description: An implementation of a Heap class for Variable Length Coding
file: heap.py
language: python3
Author: zjb
"""


class Heap(object):
    '''
    Heap that orders by a given comparison function, default to less-than.
    '''
    __slots__ = ('data', 'size', 'lessfn')

    def __init__(self, lessfn):
        '''
        Constructor takes a comparison function.
        :param lessfn: Function that takes in two heap objects and returns true
        if the first arg goes higher in the heap than the second
        '''
        self.data = []
        self.size = 0
        self.lessfn = lessfn

    def __parent(self, loc):
        '''
        Helper function to compute the parent location of an index
        :param loc: Index in the heap
        :return: Index of parent
        '''
        return (loc-1)//2

    def __bubbleUp(self, loc):
        '''
        Starts from the given location and moves the item at that spot
        as far up the heap as necessary
        :param loc: Place to start bubbling from
        '''
        while loc > 0 and self.lessfn(self.data[loc],self.data[self.__parent(loc)]):
            (self.data[loc], self.data[self.__parent(loc)]) = (self.data[self.__parent(loc)], self.data[loc])
            loc = self.__parent(loc)

    def __bubbleDown(self, loc):
        '''
        Starts from the given location and moves the item at that spot
        as far down the heap as necessary
        :param loc: Place to start bubbling from
        '''
        swapLoc = self.__smallest(loc)
        while swapLoc != loc:
            (self.data[loc], self.data[swapLoc]) = (self.data[swapLoc], self.data[loc])
            loc = swapLoc
            swapLoc = self.__smallest(loc)

    def __smallest(self, loc):
        '''
        Finds the "smallest" value of loc and loc's two children.
        Correctly handles end-of-heap issues.
        :param loc: Index
        :return: index of smallest value
        '''
        ch1 = loc*2 + 1
        ch2 = loc*2 + 2
        if ch1 >= self.size:
            return loc
        if ch2 >= self.size:
            if self.lessfn(self.data[loc],self.data[ch1]):
                return loc
            else:
                return ch1
        # now consider all 3
        if self.lessfn(self.data[ch1],self.data[ch2]):
            if self.lessfn(self.data[loc],self.data[ch1]):
                return loc
            else:
                return ch1
        else:
            if self.lessfn(self.data[loc],self.data[ch2]):
                return loc
            else:
                return ch2

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False


    def insert(self, item):
        '''
        Inserts an item into the heap.
        :param item: Item to be inserted
        '''
        self.data.append(item)
        self.size += 1
        self.__bubbleUp(self.size-1)

    def pop(self):
        '''
        Removes and returns top of the heap
        :return: Item on top of the heap
        '''
        retjob = self.data[0]
        self.size -= 1
        # if we are popping the only element, assignment will fail,
        # but bubbling is unnecessary, so:
        if self.size > 0:
            self.data[0] = self.data.pop(self.size)
            self.__bubbleDown(0)
        return retjob[1]

    def __len__(self):
        '''
        Defining the "length" of a data structure also allows it to be
        used as a boolean value!
        :return: size of heap
        '''
        return self.size

    def __str__(self):
        ret = ""
        for item in range(self.size):
            ret += str(self.data[item]) + " "
        return ret



class Graph:
    """
    A graph implemented as an adjacency list of vertices.

    :slot: vertList (dict):  A dictionary that maps a vertex key to a Vertex
        object
    :slot: numVertices (int):  The total number of vertices in the graph
    """
    def __init__(self):
        """
        Initialize the graph
        :return: None
        """
        self.edgeList = []
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """
        Add a new vertex to the graph.
        :param key: The identifier for the vertex (typically a string)
        :return: Vertex
        """
        # add the vertex to the list if it is not already present
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """
        Retrieve the vertex from the graph.
        :param key: The vertex identifier
        :return: Vertex if it is present, otherwise None
        """

        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t, cost):
        """
        Add a new directed edge from a source to a destination of an edge cost.
        :param src: The source vertex identifier
        :param dest: The destination vertex identifier
        :param cost: The edge cost (defaults to 0)
        :return: None
        """
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """
        Return the collection of vertex identifiers in the graph.
        :return: A list of vertex identifiers
        """
        return self.vertList.keys()


class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (movie name)
    """
    __slots__ = 'id','connectedTo'

    def __init__(self, key):
         self.id = key
         self.connectedTo = {}

    def addNeighbor(self, nbr, weight):
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr (Vertex): The neighbor vertex
        :param weight : The edge cost(movie name)
        :return: None
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:
            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        # Modified to include edge name(movie name)
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        """
        Get the edge cost to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: The weight
        """
        return self.connectedTo[nbr]
