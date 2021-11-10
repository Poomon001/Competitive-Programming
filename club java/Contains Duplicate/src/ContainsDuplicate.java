import java.util.*;
import java.util.stream.Collectors;

public class ContainsDuplicate {
    public static void main(String[] args){
        int[] n1 = {1,2,3,1};
        int[] n2 = {1,2,3,4};
        int[] n3 = {1,1,1,3,3,4,3,2,4,2};
        System.out.println("\n+==== Method 1 ====+\n");
        System.out.println(containsDuplicate_M1(n1)); // true
        System.out.println(containsDuplicate_M1(n2)); // false
        System.out.println(containsDuplicate_M1(n3)); // true
        System.out.println("\n+==== Method 2 ====+\n");
        System.out.println(containsDuplicate_M2(n1)); // true
        System.out.println(containsDuplicate_M2(n2)); // false
        System.out.println(containsDuplicate_M2(n3)); // true
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

    public static boolean containsDuplicate_M1(int[] nums) {
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

    /**
     * Link: https://leetcode.com/problems/contains-duplicate/
     * Purpose: Find if an array contain a duplicate
     * Parameters: int[] nums - an array of int
     * Returns: boolean - true if conatains a duplicate. Otherwise false
     * Pre-Condition: 1 <= nums.length <= 105
     *              : -109 <= nums[i] <= 109
     * Post-Condition : None
     **/
    // runtime: O(n), memory: O(n)
    public static boolean containsDuplicate_M2(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for(int num: nums){
            // found a duplicate
            if(seen.contains(num)){
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
