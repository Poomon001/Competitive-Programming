public class ArrangingCoins {
    public static void main(String[] args) {
        System.out.println("\n+==== solution M1 ====+\n");
        System.out.println(arrangeCoins_M1(5)); // 2
        System.out.println(arrangeCoins_M1(8)); // 3
        System.out.println(arrangeCoins_M1(2147483647)); // 65535
        System.out.println(arrangeCoins_M1(1)); // 1

        System.out.println("\n+==== solution M2 ====+\n");
        System.out.println(arrangeCoins_M2(5)); // 2
        System.out.println(arrangeCoins_M2(8)); // 3
        System.out.println(arrangeCoins_M2(2147483647)); // 65535
        System.out.println(arrangeCoins_M2(1)); // 1
    }

    /**
     * Link: https://leetcode.com/problems/arranging-coins/
     * Purpose: Determine the number of "completed" rows formed in a staircases (1, 2, 3 ... coins) that can fill all coins.
     * Parameters: int n - a number of coins
     * Returns: int - a number of "completed" rows
     * Pre-Condition : 1 <= n <= 23^1 - 1
     * Post-Condition  : none
     **/
    // brute force: runtime: O(n), space:O(1)
    public static int arrangeCoins_M1(int n) {
        int completedRows = 0;
        int total = n;

        // if one coin, return 1
        if(n == 1){
            return 1;
        }

        // check more than one coin
        for(int i = 1; i < total; i++){
            // subtract remainding coins with all available space in a row
            n = n - i;

            // if coin is not enough (< 0), return
            if(n < 0){
                return completedRows;
            }

            // if coin still enough then we add a row
            completedRows++;
        }
        return completedRows;
    }

    /**
     * Link: https://leetcode.com/problems/arranging-coins/
     * Purpose: Determine the number of "completed" rows formed in a staircases (1, 2, 3 ... coins) that can fill all coins.
     * Parameters: int n - a number of coins
     * Returns: int - a number of "completed" rows
     * Pre-Condition : 1 <= n <= 23^1 - 1
     * Post-Condition  : none
     **/
    // binary search: runtime: O(log(n)), space:O(1)
    // 1. we know that: 1 + 2 + 3 + ... + k rows = (k(k+1))/2 coins = n coins
    // 2. if given n coins, we could possibly form [1 to n] rows.
    public static int arrangeCoins_M2(int n) {
        long low = 1; // lowest possible row
        long high = n; // highest possible row
        while(low <= high){
            // find the middle row of lowest and highest row
            long middle = (long) Math.floor(low + (high - low)/2);

            // get the coin capacity of the middle row
            long coins = (long)Math.floor((middle*(middle+1))/2);

            // if coin capacity is higher than expected, lower the highest
            if(coins > n){
                high = middle - 1;
            // if coin capacity is lower than expected, increase the lowest
            }else if(coins <= n){
                low = middle + 1;
            }
        }

        // return the lowest row because we want only a "completed" row (now high < low)
        return (int) high;
    }
}
