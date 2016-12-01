import java.util.Scanner;

public class OneDup {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		// Reading elements of sorted array.
		int num = sc.nextInt();
		int[] arr = new int[num + 2];
		for (int counter = 0; counter < num + 2; counter++) {
			arr[counter] = sc.nextInt();
		}

		//Keeping two pointers previous and current for checking duplicate element.
		int previous = arr[0];
		int current;
		for (int counter = 1; counter < num + 2; counter++) {
			current = arr[counter];
			/*
			 * If previous & current elements are same, that means
			 * we got duplicate element. 
			 */
			if (previous == current) {
				System.out.println(current);
				break;
			} else {
				previous = current;
			}
		}
	}
}
