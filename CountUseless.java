
import java.util.ArrayList;
import java.util.Scanner;

public class CountUseless {

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int vertices, edges, vertex1, vertex2;
		int uselessCounter = 0;
		double currentCost;

		vertices = sc.nextInt();
		edges = sc.nextInt();

		double[][][] cost = new double[vertices + 1][vertices + 1][vertices + 1];
		double[][] initialCostArray = new double[vertices + 1][vertices + 1];

		for (int index1 = 1; index1 <= vertices; index1++) {
			for (int index2 = 1; index2 <= vertices; index2++) {
				if (index1 != index2) {
					cost[index1][index2][0] = Float.POSITIVE_INFINITY;
					initialCostArray[index1][index2] = Float.POSITIVE_INFINITY;
				} else {
					cost[index1][index2][0] = 0;
					initialCostArray[index1][index2] = 0;
				}
			}
		}

		for (int counter = 0; counter < edges; counter++) {
			vertex1 = sc.nextInt();
			vertex2 = sc.nextInt();
			currentCost = sc.nextFloat();
			cost[vertex1 + 1][vertex2 + 1][0] = currentCost;
			initialCostArray[vertex1 + 1][vertex2 + 1] = currentCost;
		}

		for (int index3 = 1; index3 <= vertices; index3++) {
			for (int index1 = 1; index1 <= vertices; index1++) {
				for (int index2 = 1; index2 <= vertices; index2++) {
					cost[index1][index2][index3] = Math.min(cost[index1][index2][index3 - 1],
							cost[index1][index3][index3 - 1] + cost[index3][index2][index3 - 1]);
				}
			}
		}

		for (int index1 = 1; index1 <= vertices; index1++) {
			for (int index2 = 1; index2 <= vertices; index2++) {
				if (initialCostArray[index1][index2] != Float.POSITIVE_INFINITY && index1 != index2) {
					if (initialCostArray[index1][index2] > cost[index1][index2][vertices]) {

						uselessCounter++;

					}
				}
			}
		}
		System.out.println(uselessCounter);
	}
}
