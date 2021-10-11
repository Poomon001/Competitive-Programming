public class Sqrt {
    public static void main(String[] args) {
        System.out.println(sqrt(10)); // 3
        System.out.println(sqrt(8)); // 2
        System.out.println(sqrt(4)); // 2
        System.out.println(sqrt(1)); // 1
        System.out.println(sqrt(0)); // 0
        System.out.println(sqrt(2147395600)); // 46340
        System.out.println(sqrt(2147483647)); // 46340
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
    // runtime: O(n), memory: O(1)
    public static int sqrt(int x){
        // store the previous possible solution
        int prev = 0;

        // find i where i*i is close to x from left side
        for(long i = 0; i <= x; i++){
            if(i*i == x) {
                // if i*i is x, the answer is i
                return (int) i;
            }else if(i*i > x){
                // if i*i > x, the answer is previous i
                return prev;
            }
            prev = (int) i;
        }

        // should never reach this line
        return -1;
    }
}
