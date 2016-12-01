import java.util.Scanner;

public class MergeSort {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		float[] arr = new float[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextFloat();
		}

		mergeSort(arr, 0, arr.length - 1);
	}

	public static void mergeSort(float[] arr, int first, int last) {
		if (arr.length <= 1) {
			return;
		}

		int mid = first + last / 2;
		
		float[] arr1 = new float[mid+1];
		for(int i=0; i<mid+1; i++){
			arr1[i] = arr[i];
		}
		
		float[] arr2 = new float[last-mid];
		int counter=0;
		for(int j=mid+1;j<=last;j++){
			arr2[counter] = arr[j];
			counter++;
		}

		merge(arr1, arr2);
	}
	
	public static void merge(float[] arr1, float[] arr2){
		
	}

}
