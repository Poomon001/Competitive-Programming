public class GuessNumberHigherorLower {
    public static void main(String args[]){
        System.out.println("\n === brute force solution===\n");
        long startTime = System.nanoTime();
        System.out.println("result: " + guessNumber_M1(10) + "\n");
        System.out.println("result: " + guessNumber_M1(10)  + "\n");
        System.out.println("result: " + guessNumber_M1(10)  + "\n");
        System.out.println("result: " + guessNumber_M1(10)  + "\n");
        System.out.println("result: " + guessNumber_M1(10)  + "\n");
        System.out.println("result: " + guessNumber_M1(10)  + "\n");
        System.out.println("result: " + guessNumber_M1(2126753390)  + "\n");
        System.out.println("result: " + guessNumber_M1(2126753390)  + "\n");
        System.out.println("result: " + guessNumber_M1(2126753390)  + "\n");
        System.out.println("result: " + guessNumber_M1(2126753390)  + "\n");
        System.out.println("result: " + guessNumber_M1(2126753390)  + "\n");
        long endTime   = System.nanoTime();
        long totalTime1 = endTime - startTime;

        System.out.println(" === binary search solution ===\n");
        startTime = System.nanoTime();
        System.out.println("result: " + guessNumber_M2(10) + "\n");
        System.out.println("result: " + guessNumber_M2(10)  + "\n");
        System.out.println("result: " + guessNumber_M2(10)  + "\n");
        System.out.println("result: " + guessNumber_M2(10)  + "\n");
        System.out.println("result: " + guessNumber_M2(10)  + "\n");
        System.out.println("result: " + guessNumber_M2(10)  + "\n");
        System.out.println("result: " + guessNumber_M2(2126753390)  + "\n");
        System.out.println("result: " + guessNumber_M2(2126753390)  + "\n");
        System.out.println("result: " + guessNumber_M2(2126753390)  + "\n");
        System.out.println("result: " + guessNumber_M2(2126753390)  + "\n");
        System.out.println("result: " + guessNumber_M2(2126753390)  + "\n");
        endTime   = System.nanoTime();
        long totalTime2 = endTime - startTime;
        System.out.println("Brute force total time: " + totalTime1 + " nS");
        System.out.println("Binary search total time: " + totalTime2 + " nS");
    }

    /**
     * Link: https://leetcode.com/problems/guess-number-higher-or-lower/
     * Purpose: Find a a guessing number using a private support function (read more the end of this file)
     * Parameters: int n - an integer which is an upper boundary of the random number [randomly pick a number from 1 to n]
     * Returns: int - a guessing number
     * Pre-Condition: 1 <= n <= 2^31 - 1
     *              : 1 <= randomInt <= n
     * Post-Condition : None
     * Requirment: using pow(x, 0.5) is not permitted
     **/

    // brute force (slow solution): runtime: O(n), memory: O(1)
    public static int guessNumber_M1(int n) {
        int random = (int)Math.floor(Math.random()*n)+1;
        System.out.println("expected: " + random);

        int i = 0;
        while(guessAPI(random, i) != 0){
            i++;
        }
        return i;
    }

    /**
     * Link: https://leetcode.com/problems/guess-number-higher-or-lower/
     * Purpose: Find a a guessing number using a private support function (read more the end of this file)
     * Parameters: int n - an integer which is an upper boundary of the random number [randomly pick a number from 1 to n]
     * Returns: int - a guessing number
     * Pre-Condition: 1 <= n <= 2^31 - 1
     *              : 1 <= randomInt <= n
     * Post-Condition : None
     * Requirment: using pow(x, 0.5) is not permitted
     **/

    // binary search solution (fast solution): runtime: O(log(n)), memory: O(1)
    public static int guessNumber_M2(int n) {
        int random = (int)Math.floor(Math.random()*n)+1;
        System.out.println("expected: " + random);

        long max = n;
        long min = 1;
        while(min <= max){
            // update new middle
            int middle = (int) Math.ceil((max + min)/2);

            // if the pick (middle) is less than expect
            if(guessAPI(random, middle) == -1){
                // keep the max intact, change the min to be middle+1 (+1 b/c pick (middle) is also not a possible answer)
                min = middle+1;
                continue;
            }

            // if the pick is more than expect
            if(guessAPI(random, middle) == 1){
                // keep the min intact, change the max to be middle+1 (+1 b/c pick (middle) is also not a possible answer)
                max = middle-1;
                continue;
            }

            // if the pick is expect
            if(guessAPI(random, middle) == 0){
                return middle;
            }
        }

        // answer not found
        return -1;
    }

    /**
     * purpose: determine if pick is less, more, or equal to expect
     * parameter: int expect - an expected integer
     *          : int pick - a picked integer
     * return: int - 1 if pick is less than expected
     *       : int 1 if pick is greater than expected
     *       : int 0 if pick is equal to expected
     * Pre-condition: 1 <= expect and pick <= 2^31
     * Post-condition: none
     **/
    private static int guessAPI(int expect, int pick){
        if(pick == expect){
            return 0;
        }else if(pick > expect){
            return 1;
        }else{
            return -1;
        }
    }
}
