import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class SingleNumberII {
    public static void main(String[] args){
        int[] nums1 = {2,2,3,2};
        int[] nums2 = {0,1,0,1,0,1,99};
        int[] nums3 = {0};
        int[] nums4 = {0,1,0,1,0,1,99,99,99,50};

        System.out.println("\n+==== solution M1 ====+\n");
        System.out.println(singleNumber_M1(nums1));
        System.out.println(singleNumber_M1(nums2));
        System.out.println(singleNumber_M1(nums3));
        System.out.println(singleNumber_M1(nums4));

        System.out.println("\n+==== solution M2 ====+\n");
        System.out.println(singleNumber_M2(nums1));
        System.out.println(singleNumber_M2(nums2));
        System.out.println(singleNumber_M2(nums3));
        System.out.println(singleNumber_M2(nums4));
    }
     /**
     * Link: https://leetcode.com/problems/single-number-ii/
     * Purpose: Determine a number that appear exactly one in an array where every element appears three times except for one.
     * Parameters: int[] nums - an array of integer where every element appears three times except for one.
     * Returns: int prev - an integer that appear once
     * Pre-Condition : 1 <= nums.length <= 3 * 104
     *               : -231 <= nums[i] <= 231 - 1
     *               : Each element in nums appears exactly three times except for one element which appears once.
     * Post-Condition  : none
     **/
    // two pointers solution: runtime: O(nlog(n)), memory: O(1)
    public static int singleNumber_M1(int[] nums) {
        Arrays.sort(nums);
        int i = 1;
        int prev = nums[0];
        while(i < nums.length){
            if(nums[i] == prev){
                // we need to skip the other duplicate
                i++;
                // now nums[i] is a new value
                i++;
                // set prev to a new value
                prev = nums[i];
            }else{
                break;
            }
            i++;
        }
        return prev;
    }

    /**
     * Link: https://leetcode.com/problems/single-number-ii/
     * Purpose: Determine a number that appear exactly one in an array where every element appears three times except for one.
     * Parameters: int[] nums - an array of integer where every element appears three times except for one.
     * Returns: int - an integer that appear once
     * Pre-Condition : 1 <= nums.length <= 3 * 104
     *               : -231 <= nums[i] <= 231 - 1
     *               : Each element in nums appears exactly three times except for one element which appears once.
     * Post-Condition  : none
     **/
    // hasMap solution: runtime: O(n), memory: O(n)
    public static int singleNumber_M2(int[] nums) {
        // {num, frequency}
        HashMap<Integer, Integer> seen = new HashMap();

        // count all nums in the list
        for(int num : nums){
            if(!seen.containsKey(num)){
                seen.put(num, 1);
            }else{
                seen.put(num, seen.get(num)+1);
            }
        }

        // return a num that has a counter of 1
        for (Map.Entry<Integer, Integer> data: seen.entrySet()) {
            if(data.getValue() == 1){
                return data.getKey();
            }
        }
        return -1;
    }
}
