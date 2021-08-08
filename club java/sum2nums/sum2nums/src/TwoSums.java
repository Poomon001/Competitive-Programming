// https://leetcode.com/problems/two-sum/
public class TwoSums {
    public static void main(String[] args) {
        /** solution  **/
        // 1. make a loop that go though each element in the array
        // 2. make a nest loop that goes though each elemnt in the array
        // 3. if statement to check if the sum result in the number or not. if yes return 2 indexes other whise continue the loop
        // 4. return two indices

        int [] x = {-1, 3, -5};
        int y = -6;
        for(int i = 0; i < twoSum(x,y).length; i++){
            System.out.println(twoSum(x,y)[i]);
        }
    }

    /*
     * Purpose: Indices of the two numbers such that they add up to target
     * Parameter: array - a list of integer
     *          : int - the target number
     * Returns: array - indices of two numbers such that they add up to target
     * Pre-Condition: there is always one exactly solution in the input array
     * Post-Condition: none
     */
    public static int[] twoSum(int[] nums, int target) {
        int [] x = new int[2];

        for(int i = 0; i < nums.length; i++){
            x[0] = i;
            for(int j = i + 1; j < nums.length; j++){
                if(nums[i] + nums[j] == target){
                    x[1] = j;
                    return x;
                }
            }
        }
        throw new IllegalArgumentException();
    }
}