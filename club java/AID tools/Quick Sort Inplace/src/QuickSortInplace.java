public class QuickSortInplace {

    public static void main(String[] args) {
        int []A = {1,5,2,3,9,55,44};
        A = inPlaceQuickSort(A, 0, A.length-1);
        for(int x: A){
            System.out.println(x);
        }
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

    private static void swap(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
}
