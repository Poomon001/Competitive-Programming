public class UniquePaths2 {
    public static void main(String[] args) {
        int[][] grid1 = {
                {0,0,0},
                {0,1,0},
                {0,0,0}
        };

        int[][] grid2 = {
                {0,1},
                {0,0}
        };

        int[][] grid3 = {
                {0,0,1,0},
                {0,0,1,0},
                {1,0,0,0}
        };

        int[][] grid4 = {
                {0}
        };

        int[][] grid5 = {
                {1}
        };

        int[][] grid6 = {
                {0,0,},
                {0,1,}
        };

        int[][] grid7 = {
                {0,1,0},
                {0,1,0},
                {0,1,0}
        };

        int[][] grid8 = {
                {0,0,0},
                {0,0,0},
                {0,0,0}
        };

        System.out.println(uniquePathsWithObstacles(grid1)); // 2
        System.out.println(uniquePathsWithObstacles(grid2)); // 1
        System.out.println(uniquePathsWithObstacles(grid3)); // 2
        System.out.println(uniquePathsWithObstacles(grid4)); // 1
        System.out.println(uniquePathsWithObstacles(grid5)); // 0
        System.out.println(uniquePathsWithObstacles(grid6)); // 0
        System.out.println(uniquePathsWithObstacles(grid7)); // 0
        System.out.println(uniquePathsWithObstacles(grid8)); // 6
    }

    /**
     * Link: https://leetcode.com/problems/unique-paths-ii/
     * Purpose: Find all possible unique paths to the m x n entry, where n x m grid may contain obstacles.
     *        : An obstacle and space are marked as 1 or 0 respectively in grid.
     *        : A path that the robot takes cannot include any square that is an obstacle.
     * Parameters: int[][] obstacleGrid - a n x m grid
     * Returns: int - a number of all possible paths to m x n entry
     * Pre-Condition: m == obstacleGrid.length
     *              : n == obstacleGrid[i].length
     *              : 1 <= m, n <= 100
     *              : obstacleGrid[i][j] is 0 or 1.
     * Post-Condition : None
     **/
    // dp: runtime: O(n*m), memory: O(n*m)
    public static int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // special case the first entry
        // if curr is 0 flip to top + right
        // if curr is at the edge, the edge is 0 + adjacent non-edge entry
        // if curr is 1, flip to 0

        int i = 0;
        int j = 0;
        for(i = 0; i < obstacleGrid.length; i++) {
            for(j = 0; j < obstacleGrid[0].length; j++) {
                if(i == 0 && j == 0){
                    // special case the first entry
                    obstacleGrid[0][0] = obstacleGrid[0][0] ^ 1;
                    continue;
                }

                if (obstacleGrid[i][j] == 1) {
                    // if curr is 1, flip to 0
                    obstacleGrid[i][j] = 0;
                    continue;
                }

                if(i == 0){
                    // if curr is at the edge, the edge is 0 + adjacent non-edge entry
                    obstacleGrid[0][j] += obstacleGrid[0][j - 1];
                } else if (j == 0){
                    // if curr is at the edge, the edge is 0 + adjacent non-edge entry
                    obstacleGrid[i][0] += obstacleGrid[i - 1][0];
                } else {
                    // if curr is 0 flip to top + right
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1];
                }
            }
        }
        return obstacleGrid[i - 1][j - 1];
    }
}
