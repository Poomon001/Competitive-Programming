import java.lang.reflect.Array;
import java.util.Arrays;

public class QuickSortInplace {

    public static void main(String[] args) {
        int[] A = {3,1,5,2,3,9,55,44}; // mix
        A = inPlaceQuickSort(A, 0, A.length-1);
        System.out.println(Arrays.toString(A));

        int[] B = {9, 7, 5, 3, 1}; // descending
        B = inPlaceQuickSort(B, 0, B.length-1);
        System.out.println(Arrays.toString(B));

        int[] C = {1, 2, 3, 4, 5}; // ascending
        C = inPlaceQuickSort(C, 0, C.length-1);
        System.out.println(Arrays.toString(C));

        int[] D = {-1, -12, -3, -1, -10}; // negative
        D = inPlaceQuickSort(D, 0, D.length-1);
        System.out.println(Arrays.toString(D));

        int[] E = {-5, 3, 0, -2, 1, -1};; // mix
        E = inPlaceQuickSort(E, 0, E.length-1);
        System.out.println(Arrays.toString(E));

        int[] F = {0, 0, 0, 0, 0};; // mix
        F = inPlaceQuickSort(F, 0, F.length-1);
        System.out.println(Arrays.toString(F));

        int[] G = {42};; // mix
        G = inPlaceQuickSort(G, 0, G.length-1);
        System.out.println(Arrays.toString(G));
    }

    private static int[] inPlaceQuickSort(int[] A, int l, int r){
        if(l < r){
            int p = inPlacePartition(A, l, r);
            inPlaceQuickSort(A, l, p-1);
            inPlaceQuickSort(A, p+1, r);
        }
        return A;
    }

    private static int inPlacePartition(int[] A, int l, int r){
        int p = A[r];
        int i = l;
        for(int j = l; j < r; j++) {
            if(A[j] < p) {
                swap(A, i, j);
                i++;
            }
        }
        swap(A, r, i);
        return i;
    }

    private static void swap(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
}
