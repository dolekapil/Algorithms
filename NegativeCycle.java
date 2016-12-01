
/* 
 * NegativeCycle.java 
 * 
 * Version: 1 NegativeCycle.java, v 1.1 2016/27/04 15:44:00 
 *   
 * Revisions: 
 *     Revision 1.1 Kapil 2016/27/04 18:30:19 
 */
import java.util.ArrayList;
import java.util.Scanner;

/**
 * CSCI-665 Homework 5: Problem 4 part a: This program is implementation of 
 * algorithm that determines whether the given graph contains negative cycle
 * or not. This algorithm makes use of the Dijkstra's algorithm to find the 
 * negative cycle and having running time complexity O(N2).
 *
 * @author Kapil Dole
 * @author Chirag Kular
 */
public class NegativeCycle {

	/**
	 * This method finds whether the given graph contains negative cycle or
	 * not with making assumption that graph contains exactly one negative
	 * edges. It uses Dijkstra's algorithm for finding the cycle and running
	 * time complexity of it is O(N2).
	 * 
	 * @param vertices: Total number of vertices.
	 * @param verticesList: List of vertices.
	 * @param negativeFrom: Starting vertex of negative edge.
	 * @param negativeTo: Ending vertex of negative edge.
	 * @param negativeCost: Cost of negative edge.
	 * 
	 * @return None.
	 */
	public static void findNegativeCycle(int vertices, ArrayList<Node> verticesList, int negativeFrom, int negativeTo,
			int negativeCost) {
		// Choose starting vertex as second vertex of negative edge.
		Node start = verticesList.get(negativeTo);
		// List of vertices that are not visited yet.
		ArrayList<Node> notDoneList = new ArrayList<Node>();

		// Initialize the not visited vertices list.
		for (int index = 0; index < vertices; index++) {
			notDoneList.add(verticesList.get(index));
		}

		// Removing the starting node from not done list.
		notDoneList.remove(start);
		start.cost = 0;
		update(start, verticesList, notDoneList);

		// Running the algorithm n times to make sure all of the vertices
		// get visited.
		for (int index = 0; index < vertices; index++) {
			Node nextSmallest = null;
			int smallestCost = Integer.MAX_VALUE;
			// Finding the minimum cost vertex, which is not done(visited) yet.
			for (int index2 = 0; index2 < notDoneList.size(); index2++) {
				if (smallestCost > notDoneList.get(index2).cost) {
					smallestCost = notDoneList.get(index2).cost;
					nextSmallest = notDoneList.get(index2);
				}
			}
			if (nextSmallest != null) {
				// Update the list by passing next smallest vertex as starting
				// point and remove it from the not done list.
				update(nextSmallest, verticesList, notDoneList);
				notDoneList.remove(nextSmallest);
			}
		}
		
		// If the minimum cost of the starting vertex of negative edge plus
		// edge cost is negative that means, negative cycle exists, otherwise
		// negative cycle does not exists.
		if ((verticesList.get(negativeFrom).cost + negativeCost) < 0) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}
	}

	/**
	 * This method updates the cost of every neighboring vertex of given vertex,
	 * if it is greater than current computed value.
	 * 
	 * @param vertex: The given vertex.
	 * @param verticesList: List of vertices.
	 * @param notDoneList: List of vertices which are not processed yet.
	 * 
	 * @return None.
	 */
	public static void update(Node vertex, ArrayList<Node> verticesList, ArrayList<Node> notDoneList) {
		// Updating minimum cost of every neighbor of the vertex.
		for (int index = 0; index < vertex.edgeList.size(); index++) {
			if (notDoneList.contains(verticesList.get(vertex.edgeList.get(index).get(0)))) {
				if (verticesList.get(vertex.edgeList.get(index).get(0)).cost > (vertex.edgeList.get(index).get(1))
						+ vertex.cost) {
					verticesList.get(vertex.edgeList.get(index).get(0)).cost = vertex.edgeList.get(index).get(1)
							+ vertex.cost;
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
		int vertices, edges, vertex1, vertex2, cost;
		int negativeFrom = 0, negativeTo = 0, negativeCost = 0;
		ArrayList<Node> verticesList = new ArrayList<Node>();

		vertices = sc.nextInt();
		edges = sc.nextInt();

		for (int index = 0; index < vertices; index++) {
			verticesList.add(new Node(index));
		}

		for (int counter = 0; counter < edges; counter++) {
			vertex1 = sc.nextInt();
			vertex2 = sc.nextInt();
			cost = sc.nextInt();
			
			// Storing negative edge details.
			if (cost < 0) {
				negativeCost = cost;
				negativeFrom = vertex1;
				negativeTo = vertex2;
			}

			Node node1 = verticesList.get(vertex1);
			ArrayList<Integer> vertexCost1 = new ArrayList<Integer>();
			vertexCost1.add(vertex2);
			vertexCost1.add(cost);
			node1.edgeList.add(vertexCost1);
		}

		findNegativeCycle(vertices, verticesList, negativeFrom, negativeTo, negativeCost);

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
		 * @param value: value of vertex.
		 */
		public Node(int value) {
			this.value = value;
			edgeList = new ArrayList<ArrayList<Integer>>();
			cost = Integer.MAX_VALUE;
			parent = null;
		}
	}
}
