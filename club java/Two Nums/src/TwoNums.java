import java.util.HashMap;

// https://leetcode.com/problems/two-sum/
public class TwoNums {
    public static void main(String[] args) {
        /** solution  **/
        // 1. make a loop that go though each element in the array
        // 2. make a nest loop that goes though each elemnt in the array
        // 3. if statement to check if the sum result in the number or not. if yes return 2 indexes other whise continue the loop
        // 4. return two indices

        int [] x1 = {-1, 3, -5};
        int target1 = -6;

        int [] x2 = {2,7,11,15};
        int target2 = 9;

        int [] x3 = {3,2,4};
        int target3 = 6;

        int [] x4 = {3,3};
        int target4 = 6;

        System.out.println("\n === Brute force solution ===\n");
        for(int i:twoSum_M1(x1, target1)){
            System.out.print(i + " "); // 0 2
        }

        System.out.println("");

        for(int i:twoSum_M1(x2, target2)){
            System.out.print(i + " "); // 0 1
        }

        System.out.println("");

        for(int i:twoSum_M1(x3, target3)){
            System.out.print(i + " "); // 1 2
        }

        System.out.println("");

        for(int i:twoSum_M1(x4, target4)){
            System.out.print(i + " "); // 0 1
        }

        System.out.println("\n === Hashmap solution ===\n");

        for(int i:twoSum_M2(x1, target1)){
            System.out.print(i + " "); // 0 2
        }

        System.out.println("");

        for(int i:twoSum_M2(x2, target2)){
            System.out.print(i + " "); // 0 1
        }

        System.out.println("");

        for(int i:twoSum_M2(x3, target3)){
            System.out.print(i + " "); // 1 2
        }

        System.out.println("");

        for(int i:twoSum_M2(x4, target4)){
            System.out.print(i + " "); // 0 1
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
    // brute force: runtime: O(n^2), memory: O(1)
    public static int[] twoSum_M1(int[] nums, int target) {
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

    /*
     * Purpose: Indices of the two numbers such that they add up to target
     * Parameter: array - a list of integer
     *          : int - the target number
     * Returns: array - indices of two numbers such that they add up to target
     * Pre-Condition: there is always one exactly solution in the input array
     * Post-Condition: none
     */
    // hashmap: runtime: O(n), memory: O(n)
    public static int[] twoSum_M2(int[] nums, int target) {
        // {key=diff : value=num1's index}
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[2];

        // target = num1 + num2   ==>   num2 = diff = target - num1
        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];

            // if current num1 matches any num2, we know num1 + num2 = target. We return their indices.
            if(map.containsKey(nums[i])){
                ans[0] = map.get(nums[i]);
                ans[1] = i;
                break;
            }

            // Store calculated num2 and num1's index in a map
            map.put(diff, i);
        }
        return ans;
    }
}