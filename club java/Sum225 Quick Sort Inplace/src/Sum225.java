import java.util.Scanner;
import java.util.Vector;
import java.io.File;

public class Sum225 {

    /*
     * Purpose: Determine if there are two integers in the array that sum to 225
     * Parameters: int[] A - the array of integers
     * Returns: boolean - true if a pair is found, false otherwise.
     * Preconditions: all integers in A are >= 0.
     */
    /** solution 1: brute-force O(n^2) **/
    public static boolean pairSum225_S1(int[] A){
        // Check one element with the rest of the elements if sum is 225
        for(int i: A){
            for(int j = 0; j < A.length; j++){
                if(i + A[j] == 225){
                    return true;
                }
            }
        }
        return false;
    }

    /** solution 2: inPlaceQuickSort O(n*long(n)) **/
    public static boolean pairSum225_S2(int[] A){
        // sort array first O(n*long(n))
        A = inPlaceQuickSort(A, 0, A.length-1);

        int count = 0;
        int i = 0;
        int j = A.length - 1;

        // now we have sorted array, we can scan both left (low value) and right (high value) at the same time
        // O(n)
        while(count < A.length-1){
            if(A[i] + A[j] < 225){
                // move left forward for higher sum value
                i++;
            }else if(A[i] + A[j] > 225){
                // move right backward for lower sum value
                j--;
            }else if(A[i] + A[j] == 225){
                return true;
            }
            count++;
        }

        return false;
    }

    private static int[] inPlaceQuickSort(int[] A, int l, int r){
        if(l < r){
            int p = inPlacePartition(A, l, r);
            inPlaceQuickSort(A, l, p-1);
            inPlaceQuickSort(A, p+1, r);
        }
        return A;
    }

    /* ref: https://www.geeksforgeeks.org/quick-sort/ */
    private static int inPlacePartition(int[] A, int l, int r){
        int p = A[r];
        int i = l - 1;
        for(int j = l; j <= r - 1; j++) {
            if (A[j] < p) {
                i++;
                swap(A, i, j);
            }
        }
        swap(A, i + 1, r);
        return i + 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args){
        Scanner s;

        // read input file
        try{
            File file = new File("HasPair_10.txt");
            s = new Scanner(file);
        }catch(java.io.FileNotFoundException e){
            System.out.println("Unable to open" + e);
            return;
        }

        Vector<Integer> inputVector = new Vector<Integer>();

        // store data in vector to get the size of data
        int v;
        while(s.hasNextInt() && (v = s.nextInt()) >= 0) {
            inputVector.add(v);
        }

        // store info from vector to array using data size
        int[] array = new int[inputVector.size()];

        for (int i = 0; i < array.length; i++)
            array[i] = inputVector.get(i);

        // display details of the program performance
        System.out.printf("Read %d values.\n",array.length);

        long startTime = System.currentTimeMillis();

        boolean pairExists = pairSum225_S2(array);

        long endTime = System.currentTimeMillis();

        double totalTimeSeconds = (endTime-startTime)/1000.0;

        System.out.printf("Array %s a pair of values which add to 225.\n",pairExists? "contains":"does not contain");
        System.out.printf("Total Time (seconds): %.4f\n",totalTimeSeconds);
    }
}
