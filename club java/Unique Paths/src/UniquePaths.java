public class UniquePaths {
    public static void main(String[] arg){
        System.out.println(uniquePaths(1, 1)); // 1
        System.out.println(uniquePaths(1, 3)); // 1
        System.out.println(uniquePaths(3, 1)); // 1
        System.out.println(uniquePaths(2, 2)); // 2
        System.out.println(uniquePaths(3, 3)); // 6
        System.out.println(uniquePaths(4, 4)); // 12
        System.out.println(uniquePaths(3, 7)); // 28
        System.out.println(uniquePaths(7, 3)); // 28
    }

    /**
     * Link: https://leetcode.com/problems/unique-paths/
     * Purpose: Find all possible unique paths to the mxn entry
     * Parameters: int m - a number of row
     *           : int n - a number of column
     *           : int k - an integer
     * Returns: int - a number of all possible paths to mxn entry
     * Pre-Condition: 1 <= m, n <= 100
     * Post-Condition : None
     **/
    // Dynamic programming runtime: O(n^2), memory: O(n^2)
    public static int uniquePaths(int m, int n) {
        /*
        [1 1 1]
        [1 2 3]
        [1 3 6]
        so matrix[m][n] = matrix[m][n-1] + matrix[m-1][n]
        */
        int[][] matrix = new int[m][n];

        // define the top most row
        for(int i = 0; i < n;i++){
            matrix[0][i] = 1;
        }

        // define the front most column
        for(int i = 0; i < m;i++){
            matrix[i][0] = 1;
        }

        // build a full matrix
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j];
            }
        }

        return matrix[m-1][n-1];
    }
}
