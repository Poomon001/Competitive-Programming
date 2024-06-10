import java.util.*;
import java.util.stream.Collectors;

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

        System.out.println("\n+=== solution M4 ===+\n");
        int[] nums10 = {2,2,1};
        int[] nums11 = {4,1,2,1,2};
        int[] nums12 = {1};
        System.out.println(singleNumber_M4(nums10)); // 1
        System.out.println(singleNumber_M4(nums11)); // 4
        System.out.println(singleNumber_M4(nums12)); // 1
    }

    /*
	 * Purpose: Find a single number (without other duplicate) in an array
	 * Parameter: an array - all integer elements have a duplicate but only 1 integer does not
	 * Returns: int - the only single integer in the array without duplicate
	 * Pre-Condition: there is always a single integer element in the array
	 * Post-Condition: none
	 */
    // sort - runtime: O(n(log(n))), memory: O(1)
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
    // ahshMap - runtime: O(n), memory: O(n)
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
    // XOR - runtime: O(n), memory: O(1)
    public static int singleNumber_M3(int[] nums) {
        // use XOR property I: 2 XOR 2 = 0 AND 2 XOR 0 = 2
        // use XOR property II: 2 ^ 9 ^ 2 ^ 10 ^ 10 = (2 ^ 2) ^ (10 ^ 10) ^ 9 = 9
        int ans = 0;
        for(int num:nums){
            ans = ans ^ num;
        }
        return ans;
    }

    /*
     * Purpose: Find a single number (without other duplicate) in an array
     * Parameter: an array - all integer elements have a duplicate but only 1 integer does not
     * Returns: int - the only single integer in the array without duplicate
     * Pre-Condition: there is always a single integer element in the array
     * Post-Condition: none
     */
    // set - O(n), memory: O(n)
    public static int singleNumber_M4(int[] nums) {
        int originalSum = Arrays.stream(nums).sum();
        Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int setSum = numSet.stream().mapToInt(Integer::intValue).sum();
        int ans = 2 * setSum - originalSum;
        return ans;
    }
}
