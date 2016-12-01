
/* 
 * SortingTest.java 
 * 
 * Version: 1 SortingTest.java, v 1.1 2016/10/02 17:50:40 
 *   
 * Revisions: 
 *     Revision 1.1 Kapil 2016/10/02 19:00:09 
 */
import java.util.Random;

/**
 * This program Compares the running times of the three algorithms, insertion
 * sort, merge sort and bucket sort across all different inputs.
 *
 * @author Kapil Dole
 * @author Chirag Kular
 */
public class SortingTest {

	/**
	 * This function if Merge sort implementation, where we split the input list
	 * into n lists and sort them while merging them. Time complexity of merge
	 * sort is O(N log(N)).
	 *
	 * @param 	 arr 	floating point unsorted array.
	 *            
	 * @return 	 arr   	sorted array.
	 */
	public static float[] mergeSort(float[] arr) {
		if (arr.length < 2) {
			return arr;
		}
		
		//splitting data into two equal half.
		int mid = arr.length / 2;
		float[] left_arr = new float[mid];
		System.arraycopy(arr, 0, left_arr, 0, left_arr.length);

		float[] right_arr = new float[arr.length - mid];
		System.arraycopy(arr, left_arr.length, right_arr, 0, right_arr.length);

		mergeSort(left_arr);
		mergeSort(right_arr);
		
		// merging the list and sorting while doing so.
		merge(left_arr, right_arr, arr);
		return arr;
	}

	/**
	 * This function merges two lists into single list and while doing so, it
	 * will sort the list and return single sorted list.
	 *
	 * @param   left 		  left half of unsorted array.           
	 * @param   right 		  right half of unsorted array. 
	 * @param   merged_arr    array used for storing merged sorted array.
	 *          
	 * @return None.
	 */
	public static void merge(float[] left, float[] right, float[] merged_arr) {
		int left_pointer = 0, right_pointer = 0, merged_pointer = 0;
		
		// Merging two unsorted list into single sorted list.
		while (left_pointer < left.length && right_pointer < right.length) {
			if (left[left_pointer] < right[right_pointer]) {
				merged_arr[merged_pointer] = left[left_pointer];
				left_pointer++;
			} else {
				merged_arr[merged_pointer] = right[right_pointer];
				right_pointer++;
			}
			merged_pointer++;
		}
		
		// Appending the leftover of one of two lists to sorted list.
		if (left_pointer < left.length) {
			for (int i = left_pointer; i < left.length; i++) {
				merged_arr[merged_pointer] = left[i];
				merged_pointer++;
			}
		} else if (right_pointer < right.length) {
			for (int j = right_pointer; j < right.length; j++) {
				merged_arr[merged_pointer] = right[j];
				merged_pointer++;
			}
		}

	}

	/**
	 * This function is implementation of Insertion sort algorithm, where we try
	 * to keep each sub list sorted as we traverse through list. Its time
	 * complexity is O(N2).
	 *
	 * @param   arr 	floating point unsorted array.
	 * 
	 * @return  arr 	sorted array.
	 */
	public static float[] insertionSort(float[] arr) {
		for (int i = 1; i < arr.length; i++) {
			// Element to insert.
			float temp = arr[i];
			int index = i;
			while (index > 0 && arr[index - 1] > temp) {
				arr[index] = arr[index - 1];
				index--;
			}
			arr[index] = temp;
		}
		return arr;
	}

	
	/**
	 * 
	 * This is the inner class, used for implementing buckets logic in
	 * bucket sort. 
	 *
	 */
	public static class Node {
		float value;
		Node next;

		public Node(float value) {
			this.value = value;
		}
	}

	
	/**
	 * This function is implementation of bucket sort, where we will be inserting 
	 * elements in the buckets and sort each bucket using insertion sort and finally 
	 * append all the buckets. Running time complexity of bucket sort is O(N) in 
	 * ideal case.
	 *
	 * @param   arr 	floating point unsorted array.
	 * 
	 * @return  arr 	sorted array.
	 */
	public static float[] bucketSort(float[] arr) {
		
		// Initializing buckets.
		Node[] buckets = new Node[arr.length];
		float[] sorted_arr = new float[arr.length];

		// Computing location for the element and inserting into respective bucket.
		for (int i = 0; i < arr.length; i++) {
			int loc = (int) Math.floor(arr.length * arr[i]);

			if (buckets[loc] == null) {
				buckets[loc] = new Node(arr[i]);
			} else {
				Node current = buckets[loc];
				while (current.next != null) {
					current = current.next;
				}
				current.next = new Node(arr[i]);
			}
		}

		// Running insertion sort on each individual bucket.
		for (int j = 0; j < arr.length; j++) {
			Node sorted = insertionSortOnBucket(buckets[j]);
			buckets[j] = sorted;
		}

		// Accumulating all sorted buckets into single list.
		int counter = 0;

		for (int k = 0; k < arr.length; k++) {
			if (buckets[k] != null) {
				Node current = buckets[k];
				while (current != null) {
					sorted_arr[counter] = current.value;
					counter++;
					current = current.next;
				}
			}
		}

		return sorted_arr;
	}

	
	/**
	 * This function implements insertion sort on linked list.
	 *
	 * @param   head 	first node in bucket.
	 * 
	 * @return  sorted 	sorted bucket.
	 */
	public static Node insertionSortOnBucket(Node head) {
		if (head == null) {
			return head;
		}

		Node sorted = head;
		head = head.next;
		sorted.next = null;

		while (head != null) {
			Node current = head;
			head = head.next;

			if (current.value < sorted.value) {
				current.next = sorted;
				sorted = current;
			} else {
				Node search = sorted;
				while (search.next != null && current.value > search.next.value) {
					search = search.next;
				}
				current.next = search.next;
				search.next = current;
			}
		}
		return sorted;
	}

	
	/**
	 * This function Tests the algorithms on random floating point numbers with a 
	 * Gaussian (normal) distribution with mu = 0.5 and sigma = 0.0001 .
	 *
	 * @param   n       Input size.
	 * 
	 * @return  		None.
	 */
	public static void testGaussianDistribution(int n) {
		float[] test = new float[n];
		Random rnd = new Random();
		long start, total_time;

		for (int i = 0; i < n; i++) {
			test[i] = (float) (rnd.nextGaussian() * 0.0001 + 0.5);
		}

		System.out.println("For N = " + n);
		start = System.currentTimeMillis();
		insertionSort(test);
		total_time = System.currentTimeMillis() - start;
		System.out.println("Insertion sorting time: " + total_time + " milliseconds.");

		start = System.currentTimeMillis();
		mergeSort(test);
		total_time = System.currentTimeMillis() - start;
		System.out.println("Merge sorting time: " + total_time + " milliseconds.");

		start = System.currentTimeMillis();
		bucketSort(test);
		total_time = System.currentTimeMillis() - start;
		System.out.println("Bucket sorting time: " + total_time + " milliseconds.\n");

	}

	
	/**
	 * This function Tests the algorithms on random floating point numbers with a uniform 
	 * distribution in the range [0; 1).
	 *
	 * @param   n       Input size.
	 * 
	 * @return  		None.
	 */
	public static void testNormalDistribution(int n) {

		float[] test = new float[n];
		Random rnd = new Random();
		long start, total_time;

		for (int i = 0; i < n; i++) {
			test[i] = rnd.nextFloat();
		}
		System.out.println("For N = " + n);
		start = System.currentTimeMillis();
		insertionSort(test);
		total_time = System.currentTimeMillis() - start;
		System.out.println("Insertion sorting time: " + total_time + " milliseconds.");

		start = System.currentTimeMillis();
		mergeSort(test);
		total_time = System.currentTimeMillis() - start;
		System.out.println("Merge sorting time: " + total_time + " milliseconds.");

		start = System.currentTimeMillis();
		bucketSort(test);
		total_time = System.currentTimeMillis() - start;
		System.out.println("Bucket sorting time: " + total_time + " milliseconds.\n");
	}

	
	/**
	 *  The main method.
	 *
	 *  @param       args        command line arguments (ignored)
	 */
	public static void main(String[] args) {

		System.out.println("Testing the algorithms on random floating point numbers with a uniform "
				+ "distribution in the range [0; 1).");

		testNormalDistribution(10);
		testNormalDistribution(100);
		testNormalDistribution(1000);
		testNormalDistribution(10000);
		testNormalDistribution(100000);
		testNormalDistribution(1000000);

		System.out.println(
				"Testing the algorithms on random floating point numbers with a Gaussian (normal) "
				+ "distribution with mu = 0.5 and sigma = 0.0001 .");

		testGaussianDistribution(10);
		testGaussianDistribution(100);
		testGaussianDistribution(1000);
		testGaussianDistribution(10000);
		testGaussianDistribution(100000);
		testGaussianDistribution(1000000);

	}
}
