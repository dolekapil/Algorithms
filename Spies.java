
/* 
 * Spies.java 
 * 
 * Version: 1 Spies.java, v 1.1 2016/27/04 12:54:00 
 *   
 * Revisions: 
 *     Revision 1.1 Kapil 2016/27/04 18:00:19 
 */
import java.util.ArrayList;
import java.util.Scanner;

/**
 * CSCI-665 Homework 5: Problem 3 This program is extension of basic Prim's
 * algorithm for finding the minimum cost of network. Here, the problem is we
 * have to find minimum cost of network consisting of spies as vertices. Only
 * catch is that there are some unreliable spies, so we have to find the minimum
 * cost network, such that there must not be edge from the unreliable spy. The
 * running time complexity of our algorithm is O(N2).
 *
 * @author Kapil Dole
 * @author Chirag Kular
 */
public class Spies {

	/**
	 * This method computes the minimum cost of the network considering the fact
	 * that the incoming edge should not be from the unreliable spy.
	 * 
	 * @param vertices: Total number of vertices (spies).
	 * @param verticesList: List of vertices (spies).
	 * @param unReliableList: List of unreliable vertices (spies).
	 * 
	 * @return None.
	 */
	public static void findMinCost(int vertices, ArrayList<Node> verticesList, ArrayList<Integer> unReliableList) {	
		Node start = null;
		// List of spies that are not visited yet.
		ArrayList<Node> notDoneList = new ArrayList<Node>();
		// Pick up the starting node, which is reliable spy.
		for (int index = 0; index < vertices; index++) {
			if (!unReliableList.contains(index)) {
				start = verticesList.get(index);
				break;
			}
		}
		
		// Initialize the not visited vertices list.
		for (int index = 0; index < vertices; index++) {
			notDoneList.add(verticesList.get(index));
		}
		
		// Removing the starting node.
		notDoneList.remove(start);
		start.cost = 0;
		update(start, verticesList, notDoneList);

		// Running the algorithm n times to make sure all of the vertices
		// get visited.
		for (int index = 0; index < vertices; index++) {
			Node nextSmallest = null;
			int smallestCost = Integer.MAX_VALUE;
			// Finding the minimum cost vertex, which is not done(visited) yet
			// and also it should be reliable.
			for (int index2 = 0; index2 < notDoneList.size(); index2++) {
				if (smallestCost > notDoneList.get(index2).cost
						&& !unReliableList.contains(notDoneList.get(index2).value)) {
					smallestCost = notDoneList.get(index2).cost;
					nextSmallest = notDoneList.get(index2);
				}
			}
			if (nextSmallest != null) {
				// Update the list by passing next smallest vertex as starting point
				// and remove it from the not done list.
				update(nextSmallest, verticesList, notDoneList);
				notDoneList.remove(nextSmallest);
			}
		}

		// At the last compute the total minimum cost of the network, by summing the 
		// minimum cost of each vertex and print it. If the any of node having minimum
		// cost infinity then that means minimum cost network does not exist and we
		// print NONE in this case.
		int totalMinCost = 0;
		for (int counter = 0; counter < vertices; counter++) {
			if (verticesList.get(counter).cost == Integer.MAX_VALUE) {
				System.out.println("NONE");
				System.exit(0);
			}
			totalMinCost += verticesList.get(counter).cost;
		}
		System.out.println(totalMinCost);
	}

	/**
	 * This method updates the cost of every neighboring vertex of given vertex, if 
	 * it is greater than current value.
	 * 
	 * @param vertex: The given vertex (spy).
	 * @param verticesList: List of vertices (spies).
	 * @param notDoneList: List of spies which are not processed yet.
	 * 
	 * @return None.
	 */
	public static void update(Node vertex, ArrayList<Node> verticesList, ArrayList<Node> notDoneList) {
		// Updating minimum cost of every neighbor of the vertex.
		for (int index = 0; index < vertex.edgeList.size(); index++) {
			if (notDoneList.contains(verticesList.get(vertex.edgeList.get(index).get(0)))) {
				if (verticesList.get(vertex.edgeList.get(index).get(0)).cost > vertex.edgeList.get(index).get(1)) {
					verticesList.get(vertex.edgeList.get(index).get(0)).cost = vertex.edgeList.get(index).get(1);
					verticesList.get(vertex.edgeList.get(index).get(0)).parent = vertex;
				}
			}
		}
	}

	/**
	 * The main method which takes input vertices and edges from standard input.
	 * 
	 * @param args: ignored.
	 * 
	 * @return None.
	 */
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int vertices, edges, unReliable, vertex1, vertex2, cost;
		ArrayList<Node> verticesList = new ArrayList<Node>();
		ArrayList<Integer> unReliableList = new ArrayList<Integer>();
		vertices = sc.nextInt();
		edges = sc.nextInt();
		unReliable = sc.nextInt();
		for (int counter = 0; counter < unReliable; counter++) {
			unReliableList.add(sc.nextInt());
		}

		for (int index = 0; index < vertices; index++) {
			verticesList.add(new Node(index));
		}

		for (int counter = 0; counter < edges; counter++) {
			vertex1 = sc.nextInt();
			vertex2 = sc.nextInt();
			cost = sc.nextInt();

			// Creating edge list.
			if (vertex1 != vertex2) {
				Node node1 = verticesList.get(vertex1);
				ArrayList<Integer> vertexCost1 = new ArrayList<Integer>();
				vertexCost1.add(vertex2);
				vertexCost1.add(cost);
				node1.edgeList.add(vertexCost1);

				Node node2 = verticesList.get(vertex2);
				ArrayList<Integer> vertexCost2 = new ArrayList<Integer>();
				vertexCost2.add(vertex1);
				vertexCost2.add(cost);
				node2.edgeList.add(vertexCost2);
			}
		}

		findMinCost(vertices, verticesList, unReliableList);

		sc.close();
	}

	/**
	 * This is inner class which stores information about the vertex of spy.
	 * 
	 * @author Kapil Dole.
	 * @author Chirag Kular.
	 */
	public static class Node {
		int value;
		ArrayList<ArrayList<Integer>> edgeList;
		int cost;
		Node parent;

		/**
		 * This is construction of our class used for initialization.
		 * 
		 * @param value: Number of spy.
		 */
		public Node(int value) {
			this.value = value;
			edgeList = new ArrayList<ArrayList<Integer>>();
			cost = Integer.MAX_VALUE;
			parent = null;
		}
	}
}
