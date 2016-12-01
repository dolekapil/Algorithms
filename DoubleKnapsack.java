
/* 
 * DoubleKnapsack.java 
 * 
 * Version: 1 DoubleKnapsack.java, v 1.1 2016/16/03 15:50:46 
 *   
 * Revisions: 
 *     Revision 1.1 Kapil 2016/10/02 18:00:19 
 */
import java.util.Scanner;

/**
 * CSCI-665 Homework 3: Problem 5
 * This program is extension of basic knapsack problem, where we have to select
 * set of items with maximum cost that fits in the two backpacks. This problem
 * we have solved using dynamic programming and its running time complexity is
 * O(n * W1 * W2).
 *
 * @author Kapil Dole
 * @author Chirag Kular
 */
public class DoubleKnapsack {

	/**
	 * 
	 * This function takes total number of items, their weight, cost and cost of
	 * both knapsack and then finds the set of items that fits the both knapsack
	 * such that cost is maximum using dynamic programming, we making use of
	 * overlapping sub problem to solve our current problem.
	 * 
	 * @param 		n		Total number of items.
	 * @param 		W1		Capacity of knapsack 1.
	 * @param 		W2		Capacity of knapsack 2.
	 * @param 		WiCi	weight and cost table for each item.
	 * 
	 * @return 		Maximum cost of a set of items that fits in the two backpacks.
	 */
	public static int knapsack(int n, int W1, int W2, int[][] WiCi) {

		// To solve double knapsack we are going to need 3D array.
		int[][][] S = new int[n + 1][W1 + 1][W2 + 1];
		int previousMax, knapsack1, knapsack2;
		for (int index1 = 1; index1 < n + 1; index1++) {
			for (int index2 = 0; index2 < W1 + 1; index2++) {
				for (int index3 = 0; index3 < W2 + 1; index3++) {
					// Getting maximum value of previous sub problem.
					previousMax = S[index1 - 1][index2][index3];
					knapsack1 = 0;
					knapsack2 = 0;

					// getting total cost by putting current item into knapsack 1.
					if (WiCi[index1 - 1][0] <= index2) {
						knapsack1 = S[index1 - 1][index2 - WiCi[index1 - 1][0]][index3] + WiCi[index1 - 1][1];
					}
					// getting total cost by putting current item into knapsack 2.
					if (WiCi[index1 - 1][0] <= index3) {
						knapsack2 = S[index1 - 1][index2][index3 - WiCi[index1 - 1][0]] + WiCi[index1 - 1][1];
					}
					
					// Setting maximum of all three values to the current index in our 3D array.
					S[index1][index2][index3] = Math.max(previousMax, Math.max(knapsack1, knapsack2));
				}
			}
		}
		// Returning last element of our 3D array which contains optimal solution.
		return S[n][W1][W2];
	}

	/**
	 *  The main method which takes input from standard input.
	 *
	 *  @param       args        command line arguments (ignored)
	 */
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n, W1, W2;
		// Taking input for n, W1 and W2.
		n = sc.nextInt();
		W1 = sc.nextInt();
		W2 = sc.nextInt();

		// Storing weight and cost values for each item in array.
		int[][] WiCi = new int[n][2];
		for (int index = 0; index < n; index++) {
			WiCi[index][0] = sc.nextInt();
			WiCi[index][1] = sc.nextInt();
		}

		// Displaying optimal result.
		System.out.println(knapsack(n, W1, W2, WiCi));
		sc.close();
	}
}
