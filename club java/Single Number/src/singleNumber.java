import java.util.*;

// https://leetcode.com/problems/single-number/
public class singleNumber {
    public static void main(String[] args){
        System.out.println("\n+=== solution M1 ===+\n");
        int[] nums1 = {2,2,1};
        int[] nums2 = {4,1,2,1,2};
        int[] nums3 = {1};
        System.out.println(singleNumber_M1(nums1)); // 1
        System.out.println(singleNumber_M1(nums2)); // 4
        System.out.println(singleNumber_M1(nums3)); // 1

        System.out.println("\n+=== solution M2 ===+\n");
        int[] nums4 = {2,2,1};
        int[] nums5 = {4,1,2,1,2};
        int[] nums6 = {1};
        System.out.println(singleNumber_M2(nums4)); // 1
        System.out.println(singleNumber_M2(nums5)); // 4
        System.out.println(singleNumber_M2(nums6)); // 1

        System.out.println("\n+=== solution M3 ===+\n");
        int[] nums7 = {2,2,1};
        int[] nums8 = {4,1,2,1,2};
        int[] nums9 = {1};
        System.out.println(singleNumber_M3(nums7)); // 1
        System.out.println(singleNumber_M3(nums8)); // 4
        System.out.println(singleNumber_M3(nums9)); // 1
    }

    /*
	 * Purpose: Find a single number (without other duplicate) in an array
	 * Parameter: an array - all integer elements have a duplicate but only 1 integer does not
	 * Returns: int - the only single integer in the array without duplicate
	 * Pre-Condition: there is always a single integer element in the array
	 * Post-Condition: none
	 */
    // runtime: O(n(log(n))), memory: O(1)
    public static int singleNumber_M1(int[] nums) {
        // sort to make it easier to handle array
        Arrays.sort(nums);
        int i = 0;

        while(i+1 < nums.length){
            if(nums[i] == nums[i+1]){
                // skip to next pair
                i += 2;
            }else{
                return nums[i];
            }
        }
        // every pair so far contains the two numbers, so the last element must be the answer
        return nums[nums.length-1];
    }

    /*
     * Purpose: Find a single number (without other duplicate) in an array
     * Parameter: an array - all integer elements have a duplicate but only 1 integer does not
     * Returns: int - the only single integer in the array without duplicate
     * Pre-Condition: there is always a single integer element in the array
     * Post-Condition: none
     */
    // runtime: O(n), memory: O(n)
    public static int singleNumber_M2(int[] nums) {
        // {num, frequency}
        HashMap<Integer, Integer> seen = new HashMap();

        // get all elements to the map key with value of its frequency
        for(int num:nums){
            if(seen.containsKey(num)){
                seen.put(num, seen.get(num)+1);
            }else{
                seen.put(num, 1);
            }
        }

        // find an element with a frequency of 1
        for(Map.Entry<Integer, Integer> data:seen.entrySet()){
            if(data.getValue() == 1){
                return data.getKey();
            }
        }
        return -1;
    }

    /*
     * Purpose: Find a single number (without other duplicate) in an array
     * Parameter: an array - all integer elements have a duplicate but only 1 integer does not
     * Returns: int - the only single integer in the array without duplicate
     * Pre-Condition: there is always a single integer element in the array
     * Post-Condition: none
     */
    // runtime: O(n), memory: O(1)
    public static int singleNumber_M3(int[] nums) {
        int ans = nums[0];

        // xor N and N is 0, and xor 0 and N is N
        for(int i = 1; i < nums.length; i++) {
            ans = ans^nums[i];
        }
        return ans;
    }
}
