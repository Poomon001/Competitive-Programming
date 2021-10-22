import java.util.Arrays;

public class ContainsDuplicate {
    public static void main(String[] args){
        int[] n1 = {1,2,3,1};
        int[] n2 = {1,2,3,4};
        int[] n3 = {1,1,1,3,3,4,3,2,4,2};
        System.out.println(containsDuplicate(n1)); // true
        System.out.println(containsDuplicate(n2)); // false
        System.out.println(containsDuplicate(n3)); // true
    }

    /**
     * Link: https://leetcode.com/problems/contains-duplicate/
     * Purpose: Find if an array contain a duplicate
     * Parameters: int[] nums - an array of int
     * Returns: boolean - true if conatains a duplicate. Otherwise false
     * Pre-Condition: 1 <= nums.length <= 105
     *              : -109 <= nums[i] <= 109
     * Post-Condition : None
     **/
    // runtime: O(n), memory: O(1)
    public static boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int prev = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if(prev == nums[i]){
                return true;
            }
            prev = nums[i];
        }

    return false;
    }
}
