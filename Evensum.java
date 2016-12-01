
/* 
 * Evensum.java 
 * 
 * Version: 1 Evensum.java, v 1.1 2016/28/01 00:58:40 
 *   
 * Revisions: 
 *     Revision 1.1 Kapil 2016/28/01 00:59:40    
 */
import java.util.Scanner;

/**
 * This program takes non-negative integers as input and prints out the sum of
 * all inputs that are even.
 *
 * @author Kapil Dole
 */
public class Evensum {

	public static void main(String[] args) {

		// Taking input from Standard Input.
		Scanner sc = new Scanner(System.in);
		int total_num = sc.nextInt();

		int even_sum = 0;
		// Calculating even input sum.
		for (int i = 0; i < total_num; i++) {
			int num = sc.nextInt();
			if (num % 2 == 0) {
				even_sum += num;
			}
		}
		System.out.println(even_sum);
	}
}
