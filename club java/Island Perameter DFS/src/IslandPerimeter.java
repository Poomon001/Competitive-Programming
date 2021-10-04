import java.util.*;

public class IslandPerimeter {
    public static void main(String[] args) {
        int[][] grid1 = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}};
        System.out.println(islandParameter(grid1));// 16

        int[][]  grid2 = {{ 1 }};
        System.out.println(islandParameter(grid2)); // 4

        int[][] grid3 = {{0, 1}};
        System.out.println(islandParameter(grid3)); // 4
    }

    /*
    * Link: https://leetcode.com/problems/island-perimeter/
    * Purpose: Grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
    *        : Find the perimeter of the island.
    * Parameters: int[][] grid - a 2D array represents a map where Grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
    * Returns: int[] parameter - parameter of the island
    * Pre-Condition: row == grid.length
                   : col == grid[i].length
                   : 1 <= row, col <= 100
                   : grid[i][j] is 0 or 1.
                   : There is exactly one island in grid.
      Post-Condition : None
    */

    // runtime: O(n*m), memory:O(1)
    public static int islandParameter(int[][] grid) {
        int parameter = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[i].length;j++){
                // for every land (grid[i][j] == 1), count parameter
                if(grid[i][j] == 1){
                    // left side of the curr land is the boundary(index out of bound == j-1 < 0 or water(grid[i][j] == 0) add 1 to parameter
                    if (j-1 < 0 || grid[i][j-1] == 0){
                        parameter += 1;
                    }

                    // right side of the curr land is the boundary(index out of bound == j+1 > grid[i].length - 1 or water(grid[i][j] == 0) add 1 to parameter
                    if (j+1 > grid[i].length - 1 || grid[i][j+1] == 0){
                        parameter += 1;
                    }

                    // buttom of the curr land is the boundary(index out of bound == i-1 < 0 or water(grid[i][j] == 0) add 1 to parameter
                    if (i-1 < 0 || grid[i-1][j] == 0){
                        parameter += 1;
                    }

                    // top of the curr land is the boundary(index out of bound == i-1 > grid.length - 1 or water(grid[i][j] == 0) add 1 to parameter
                    if (i+1 > grid.length - 1 || grid[i+1][j] == 0){
                        parameter += 1;
                    }
                }
            }
        }
        return parameter;
    }
}
