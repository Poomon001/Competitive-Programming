import java.util.*;

public class IslandPerimeter {
    public static void main(String[] args) {
        int[][] grid1 = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}};
        int[][]  grid2 = {{ 1 }};
        int[][] grid3 = {{0, 1}};

        System.out.println("\n === Solution 1 === \n");
        System.out.println(islandPerimeter_M1(grid1));// 16
        System.out.println(islandPerimeter_M1(grid2)); // 4
        System.out.println(islandPerimeter_M1(grid3)); // 4

        System.out.println("\n === Solution 2 === \n");
        System.out.println(islandPerimeter_M2(grid1));// 16
        System.out.println(islandPerimeter_M2(grid2)); // 4
        System.out.println(islandPerimeter_M2(grid3)); // 4
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
    // 2D array - runtime: O(n*m), memory:O(1)
    public static int islandPerimeter_M1(int[][] grid) {
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int perimeter = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    for (int[] dir : directions) {
                        int new_i = i + dir[0];
                        int new_j = j + dir[1];

                        if (new_i < 0 || new_i >= grid.length || new_j < 0 || new_j >= grid[0].length || grid[new_i][new_j] == 0) {
                            perimeter++;
                        }
                    }
                }
            }
        }

        return perimeter;
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
    // dfs - runtime: O(n*m), memory:O(K) where k = blocks of lands
    static int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int perimeter = 0;
    Set<String> visited = new HashSet<>();

    public void dfs(int[][] grid, int i, int j) {
        String key = i + "," + j;

        if (visited.contains(key)) return;

        visited.add(key);

        for(int[] direction:directions) {
            int new_i = i + direction[0];
            int new_j = j + direction[1];
            String new_key = new_i + "," + new_j;
            if (new_i < 0 || new_i >= grid.length || new_j < 0 || new_j >= grid[0].length || grid[new_i][new_j] == 0) {
                perimeter++;
            } else {
                if(!visited.contains(new_key)) {
                    dfs(grid, new_i, new_j);
                }
            }
        }
    }

    public static int islandPerimeter_M2(int[][] grid) {
        IslandPerimeter s = new IslandPerimeter();
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[i].length; j++) {
                if(grid[i][j] == 1) {
                    s.dfs(grid, i, j);
                    return s.perimeter;
                }
            }
        }
        // no land
        return 0;
    }
}
