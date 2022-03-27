import java.util.*;
public class TheKWeakestRowsInAMatrix {
    /**
     * Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
     * Purpose: Find the indices of the k weakest rows in the matrix ordered from weakest to strongest.
     *        :A row i is weaker than a row j if one of the following is true:
     *            1. The number of soldiers in row i is less than the number of soldiers in row j.
     *            2. Both rows have the same number of soldiers and i < j.
     * Parameters: int[][] mat - a 2D interger arrays
     *           : int k - an integer
     * Returns: int[] answer - the indices of the k weakest rows in the matrix ordered from weakest to strongest
     * Pre-Condition: m == mat.length
     *              : n == mat[i].length
     *              : 2 <= n, m <= 100
     *              : 1 <= k <= m
     *              : matrix[i][j] is either 0 or 1
     * Post-Condition : None
     **/
    public static void main(String[] args) {
        int[][] mat1 = {{1,1,0,0,0}, {1,1,1,1,0}, {1,0,0,0,0}, {1,1,0,0,0}, {1,1,1,1,1}};
        int[][] mat2 = {{1,0,0,0}, {1,1,1,1}, {1,0,0,0}, {1,0,0,0}};
        int[][] mat3 = {{1}};

        for(int i:kWeakestRows(mat1, 3)){
            System.out.print(i + " "); // 2 0 3
        }
        System.out.println("");

        for(int i:kWeakestRows(mat2, 2)){
            System.out.print(i + " "); // 0 2
        }
        System.out.println("");

        for(int i:kWeakestRows(mat3, 1)){
            System.out.print(i + " "); // 0
        }
    }

    public static int[] kWeakestRows(int[][] mat, int k) {
        // [[sum, row],]
        int[][] weakest = new int[mat.length][2];
        for(int i = 0; i < mat.length; i++){
            int sum = 0;
            for(int j = 0; j < mat[i].length; j++){
                sum += mat[i][j];
            }
            weakest[i][0] = sum;
            weakest[i][1] = i;
        }
        Arrays.sort(weakest, (a, b) -> a[0] - b[0]);
        int[] answer = new int[k];
        for(int i = 0; i < k;i++){
            answer[i] = weakest[i][1];
        }
        return answer;
    }
}
