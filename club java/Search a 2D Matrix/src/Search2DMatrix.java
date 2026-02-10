public class Search2DMatrix {
    public static void main(String[] args) {
        int[][] matrix1 = new int[][]{{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        int[][] matrix2 = new int[][]{{2,3,5,7},{10,11,16,20},{23,30,34,60},{61,130,314,610}};

        System.out.println("\n === solution 1 \n");
        System.out.println(searchMatrix_M1(matrix1, 3)); // true
        System.out.println(searchMatrix_M1(matrix1, 13)); // false

        System.out.println(searchMatrix_M1(matrix2, 13)); // false
        System.out.println(searchMatrix_M1(matrix2, 1)); // false
        System.out.println(searchMatrix_M1(matrix2, 1000)); // false
        System.out.println(searchMatrix_M1(matrix2, 2)); // true
        System.out.println(searchMatrix_M1(matrix2, 610)); // true
        System.out.println(searchMatrix_M1(matrix2, 20)); // true

        System.out.println("\n === solution 2 \n");
        System.out.println(searchMatrix_M2(matrix1, 3)); // true
        System.out.println(searchMatrix_M2(matrix1, 13)); // false

        System.out.println(searchMatrix_M2(matrix2, 13)); // false
        System.out.println(searchMatrix_M2(matrix2, 1)); // false
        System.out.println(searchMatrix_M2(matrix2, 1000)); // false
        System.out.println(searchMatrix_M2(matrix2, 2)); // true
        System.out.println(searchMatrix_M2(matrix2, 610)); // true
        System.out.println(searchMatrix_M2(matrix2, 20)); // true
    }

    /**
        Link: https://leetcode.com/problems/search-a-2d-matrix
        Purpose: find if a target in 2-d array given the 2-d array of integer sorted from left to right and up to bottom
        parameter: List[List[int] matrix - the sorted 2-d array
                 : int target - an integer
        return: bool - if the targer is in the 2-d array. Otherwise False.
        Pre-Condition: m == matrix.length
                     : n == matrix[i].length
                     : 1 <= m, n <= 100
                     : -10^4 <= matrix[i][j], target <= 10^4
        Post-Condition: none
    **/
    // 2-level binary search - runtime: O(log(m) + log(n)), memory: O(1)
    public static boolean searchMatrix_M1(int[][] matrix, int target) {
        // search for the possible row
        int top = 0;
        int bottom = matrix.length - 1;
        int row = 0;

        while(top <= bottom) {
            int mid = (int)((bottom - top) / 2 + top);

            if(matrix[mid][0] <= target && target <= matrix[mid][matrix[0].length - 1]) {
                row = mid;
            }

            if(target > matrix[mid][0]) {
                top = mid + 1;
            } else {
                bottom = mid - 1;
            }
        }

        // search for the target within the possible row
        int left = 0;
        int right = matrix[row].length - 1;
        while(left <= right) {
            int mid = (int)((right - left) / 2 + left);

            if(matrix[row][mid] == target) {
                return true;
            }

            if(target > matrix[row][mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }

    public static boolean searchMatrix_M2(int[][] matrix, int target) {
        int n = matrix.length;
        int m = matrix[0].length;

        /**
         * [[1, 3, 5],
         * [7, 9, 11],
         * [13, 15, 17]]
         * [1, 3, 5, 7, 9, 11, 13, 15, 17]
         *  l                           r
        **/
        int left = 0;
        int right = n * m - 1;

        while(left <= right) {
            int mid = ((right - left) / 2) + left;

            // 2D search trick
            int row = mid / m;
            int col = mid % m;
            int value = matrix[row][col];

            if (target == value) {
               return true;
            }
            if (target > value) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
