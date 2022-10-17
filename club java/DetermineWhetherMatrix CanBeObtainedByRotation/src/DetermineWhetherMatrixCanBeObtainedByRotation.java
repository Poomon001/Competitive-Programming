import java.awt.geom.AffineTransform;
import java.util.Arrays;

public class DetermineWhetherMatrixCanBeObtainedByRotation {
    public static void main(String[] args) {
        int[][] matrix1 = {{1,2,3}, {0,0,0}, {4,5,6}};
        int[][] matrix2 = {{1,2,3}, {0,0,0}, {4,5,6}};
        int[][] matrix3 = {{4,0,1}, {5,0,2}, {6,0,3}};
        int[][] matrix4 = {{6,5,4}, {0,0,0}, {3,2,1}};
        int[][] matrix5 = {{0,0,0}, {6,5,4}, {3,2,1}}; // not 90 degree

        int[][] matrix6 = {{1,2}, {0,0}};
        int[][] matrix7 = {{0,1}, {0,2}};
        int[][] matrix8 = {{0,0}, {2,1}};
        int[][] matrix9 = {{2,0}, {1,0}};
        int[][] matrix10 = {{1,2}, {0,0}};
        int[][] matrix11 = {{1,0}, {2,0}}; // not 90 degree

        int[][] matrix12 = {{4,0,1,4}, {5,0,2,6}, {6,0,3,1}, {0,0,0,0}};
        int[][] matrix13 = {{0,6,5,4}, {0,0,0,0}, {0,3,2,1}, {0,1,6,4}};
        int[][] matrix14 = {{0,0,0,0}, {1,3,0,6}, {6,2,0,5}, {4,1,0,4}};
        int[][] matrix15 = {{4,0,1,4}, {5,0,2,6}, {0,0,0,0}, {6,0,3,1}};// not 90 degree

        System.out.println("\n+=== solution 1 ===+\n");
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix1, matrix2)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix1, matrix3)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix1, matrix4)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix4, matrix1)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix1, matrix5)); // false
        System.out.println("");
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix6, matrix7)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix7, matrix8)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix10, matrix9)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix9, matrix7)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix8, matrix10)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix11, matrix9)); // false
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix11, matrix10)); // false
        System.out.println("");
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix12, matrix13)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix13, matrix14)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix12, matrix15)); // false
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m1(matrix15, matrix13)); // false

        matrix1 = new int[][] {{1,2,3}, {0,0,0}, {4,5,6}};
        matrix2 = new int[][] {{1,2,3}, {0,0,0}, {4,5,6}};
        matrix3 = new int[][] {{4,0,1}, {5,0,2}, {6,0,3}};
        matrix4 = new int[][] {{6,5,4}, {0,0,0}, {3,2,1}};
        matrix5 = new int[][] {{0,0,0}, {6,5,4}, {3,2,1}}; // not 90 degree

        matrix6 = new int[][] {{1,2}, {0,0}};
        matrix7 = new int[][] {{0,1}, {0,2}};
        matrix8 = new int[][] {{0,0}, {2,1}};
        matrix9 = new int[][] {{2,0}, {1,0}};
        matrix10 = new int[][] {{1,2}, {0,0}};
        matrix11 = new int[][] {{1,0}, {2,0}}; // not 90 degree

        matrix12 = new int[][] {{4,0,1,4}, {5,0,2,6}, {6,0,3,1}, {0,0,0,0}};
        matrix13 = new int[][] {{0,6,5,4}, {0,0,0,0}, {0,3,2,1}, {0,1,6,4}};
        matrix14 = new int[][] {{0,0,0,0}, {1,3,0,6}, {6,2,0,5}, {4,1,0,4}};
        matrix15 = new int[][] {{4,0,1,4}, {5,0,2,6}, {0,0,0,0}, {6,0,3,1}};// not 90 degree

        System.out.println("\n+=== solution 2 ===+\n");
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix1, matrix2)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix1, matrix3)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix1, matrix4)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix4, matrix1)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix1, matrix5)); // false
        System.out.println("");
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix6, matrix7)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix7, matrix8)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix10, matrix9)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix9, matrix7)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix8, matrix10)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix11, matrix9)); // false
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix11, matrix10)); // false
        System.out.println("");
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix12, matrix13)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix13, matrix14)); // true
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix12, matrix15)); // false
        System.out.println(determineWhetherMatrixCanBeObtainedByRotation_m2(matrix15, matrix13)); // false
    }

    /**
     * Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/
     * Purpose: Determine Whether Matrix Can Be Obtained By Rotations (90 degree each)
     * Parameter: int[][] matrix - a given matrix (2d array)
     *          : int[][] target - a target matrix (2d array)
     * Returns: boolean: true if the target can be obtained by Rotation. Otherwise, false.
     * Pre-Condition: n == mat.length == target.length
     *              : n == mat[i].length == target[i].length
     *              : 1 <= n <= 10
     *              : mat[i][j] and target[i][j] are either 0 or 1.
     * Post-Condition: none
     **/
    // run-time: O(n^2), memory: O(n^2)
    public static boolean determineWhetherMatrixCanBeObtainedByRotation_m1(int[][] matrix, int[][] target){
        int len = matrix.length;
        int[][] temp = new int[len][len];
        for(int k = 0; k <= 4; k++) {
            for (int i = 0; i < len; i++) {
                for (int j = 0; j < len; j++) {
                    temp[j][len - 1 - i] = matrix[i][j];
                }
            }
            if (Arrays.deepEquals(temp, target)) {
                return true;
            } else {
                for(int j = 0; j < len; j++) {
                    matrix[j] = Arrays.copyOf(temp[j], len);
                }
            }
        }
        return false;
    }

    /**
     * Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/
     * Purpose: Determine Whether Matrix Can Be Obtained By Rotations (90 degree each)
     * Parameter: int[][] matrix - a given matrix (2d array)
     *          : int[][] target - a target matrix (2d array)
     * Returns: boolean: true if the target can be obtained by Rotation. Otherwise, false.
     * Pre-Condition: n == mat.length == target.length
     *              : n == mat[i].length == target[i].length
     *              : 1 <= n <= 10
     *              : mat[i][j] and target[i][j] are either 0 or 1.
     * Post-Condition: none
     **/
    // run-time: O(n^2), memory: O(1)
    public static boolean determineWhetherMatrixCanBeObtainedByRotation_m2(int[][] matrix, int[][] target){
        int len = matrix.length;
        for(int k = 0; k <= 4; k++) {
            for (int i = 0; i < len/2; i++) {
                int last = len - 1 - i;
                for (int j = i; j < last; j++) {
                    int offset = j - i;
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[last - offset][i];
                    matrix[last - offset][i] = matrix[last][last-offset];
                    matrix[last][last - offset] = matrix[j][last];
                    matrix[j][last] = temp;
                }
            }
            if (Arrays.deepEquals(matrix, target)) {
                return true;
            }
        }
        return false;
    }
}
