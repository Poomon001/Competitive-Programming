public class MaxConstructiveOnes {
    public static void main(String[] args) {
        int[] t1 = {1,1,0,1,1,1};
        System.out.println(maxConsecutiveOnes(t1)); // 3

        int[] t2 = {1,0,1,1,0,1};
        System.out.println(maxConsecutiveOnes(t2)); //2
    }

    /*
     * Link: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3982/
     * Purpose: Find the maximum number of consecutive 1's in the array.
     * Parameters: int[] - a list of 1s and 0s
     * Returns: int - the maximum number of consecutive 1's in the array
     * Pre-Condition: 1 <= nums.length <= 105
                    : nums[i] is either 0 or 1.
       Post-Condition : None
     */
    // greedy: O(n)
    public static int maxConsecutiveOnes(int[] nums){
        // store current max consecutive count
        int conter = 0;

        // store global max consecutive count
        int maxCounter = 0;

        for (int i = 0; i < nums.length; i++){
            if(nums[i] == 1){
                // inclement count by 1 if the num is 1
                conter++;
            }else{
                // reset count to 0 if the num is 0
                conter = 0;
            }

            // update global maximun
            maxCounter = conter>maxCounter?conter:maxCounter;
        }
        return maxCounter;
    }
}
