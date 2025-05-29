public class Sqrt {
    public static void main(String[] args) {
        System.out.println("\n === Solution 1 === \n");
        System.out.println(sqrt_M1(2147395600)); // 46340
        System.out.println(sqrt_M1(2147483647)); // 46340
        System.out.println(sqrt_M1(101)); // 10
        System.out.println(sqrt_M1(1)); // 1
        System.out.println(sqrt_M1(0)); // 0
        System.out.println(sqrt_M1(8)); // 2
        System.out.println(sqrt_M1(4)); // 2

        System.out.println("\n === Solution 2 === \n");
        System.out.println(sqrt_M2(2147395600)); // 46340
        System.out.println(sqrt_M2(2147483647)); // 46340
        System.out.println(sqrt_M2(101)); // 10
        System.out.println(sqrt_M2(1)); // 1
        System.out.println(sqrt_M2(0)); // 0
        System.out.println(sqrt_M2(8)); // 2
        System.out.println(sqrt_M2(4)); // 2
    }

    /**
     * Link: https://leetcode.com/problems/sqrtx/
     * Purpose: Find a floor of sqrt of x
     * Parameters: int x - an integer
     * Returns: int - a floor integer sqrt of x
     * Pre-Condition: 0 <= x <= 231 - 1
     * Post-Condition : None
     * Requirment: using pow(x, 0.5) is not permitted
     **/
    // runtime: O(n*n^2), memory: O(1)
    public static int sqrt_M2(int x){
        int num = x;
        for(int i = 0; i <= num; i++) {
            long pow = (long) i * i;
            if(pow >= x){
                if(pow == x) {
                    return i;
                }
                return i - 1;
            }
        }

        return 0;
    }

    /**
     * Link: https://leetcode.com/problems/sqrtx/
     * Purpose: Find a floor of sqrt of x
     * Parameters: int x - an integer
     * Returns: int - a floor integer sqrt of x
     * Pre-Condition: 0 <= x <= 231 - 1
     * Post-Condition : None
     * Requirment: using pow(x, 0.5) is not permitted
     **/
    // runtime: O(log(n)*n^2), memory: O(1)
    public static int sqrt_M1(int x){
        int i = 0;
        int j = x;

        while(i <= j){
            int mid = (j - i) / 2 + i;
            long pow = (long) mid * mid;
            if(pow == x) {
                return mid;
            }
            if(pow > x) {
                j = mid -1;
            }else{
                i = mid +1;
            }
        }

        return j;
    }
}
