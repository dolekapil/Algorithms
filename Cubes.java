
/* 
 * Cubes.java 
 * 
 * Version: 1 Cubes.java, v 1.1 2016/28/01 00:50:40 
 *   
 * Revisions: 
 *     Revision 1.1 Kapil 2016/28/01 00:50:40 
 */
import java.util.Scanner;

/**
 * This program print out all cubes in increasing order, starting from 0, that
 * are less than or equal to the input value.
 *
 * @author Kapil Dole
 */
public class Cubes {

	public static void main(String[] args) {
		
		// Taking input from Standard Input.
		Scanner sc = new Scanner(System.in);
		int input = sc.nextInt();

		int cubes, counter = 0;
		// Printing cube values less than input.
		while (true) {
			cubes = (int) Math.pow(counter, 3);
			if (cubes > input) {
				break;
			}
			System.out.println(cubes);
			counter++;
		}
	}
}
