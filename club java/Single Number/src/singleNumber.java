import java.util.Arrays;

// https://leetcode.com/problems/single-number/
public class singleNumber {
    public static void main(String[] args){
        int[] x = {2,2,1};
        int[] y = {4,1,2,1,2};
        int[] z = {1};
        System.out.println(singleNumber(x)); // 1
        System.out.println(singleNumber(y)); // 4
        System.out.println(singleNumber(z)); // 1
    }

    /*
	 * Purpose: Find a single number (without other duplicate) in an array
	 * Parameter: an array - all integer elements have a duplicate but only 1 integer does not
	 * Returns: int - the only single integer in the array without duplicate
	 * Pre-Condition: there is always a single integer element in the array
	 * Post-Condition: none
	 */
    // runtime: O(n(log(n))), memory: O(1)
    public static int singleNumber(int[] nums) {
        // if there is only one number then return
        if(nums.length == 1){
            return nums[0];
        }

        // sort to make it easier to handle array
        Arrays.sort(nums);
        for(int i = 0; i < nums.length-1; i++){
            // if a pair of two numbers in a sorted array are equal then they both not the answer
            if(nums[i] == nums[i+1]){
                // skip both
                i++;
            }else{
                // if a pair is not equal then we know that the former number is the answer
                return nums[i];
            }
        }

        // because the array has an odd n integers, the last number will not get compared by the above loop
        // However, we know that there is a garanteed solution, so if the above loop cannot get the answer, then the answer
        // is garuntee to be the last number
        return nums[nums.length-1];

    }
}
