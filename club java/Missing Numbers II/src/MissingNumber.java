import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class MissingNumber {
    public static void main(String[] args) {
        int[] nums1 = {3,0,1};
        System.out.println(missingNumber(nums1));

        int[] nums2 = {0,1};
        System.out.println(missingNumber(nums2));
    }

    /*
    * Link: https://leetcode.com/problems/missing-number/
    * Purpose: Find the only number in the range that is missing from the array.
    * Parameters: int [] - a sequence of integer from o to n
    * Returns: int - a missing interger in the sequence
    * Pre-Condition: n == nums.length
                   : 1 <= n <= 104
                   : 0 <= nums[i] <= n
                   : All the numbers of nums are unique.
      Post-Condition : None
    */

    // sort: runtime: O(nlog(n)), memory: O(1)
    public static int missingNumber_M1(int[] nums) {
        Arrays.sort(nums);
        // Chack if there is any missing element
        for(int i = 0; i < nums.length; i++){
            if(i != nums[i]){
                return i;
            }
        }
        // if no missing element return the highest number + 1
        return nums[nums.length-1]+1;
    }

    /*
    * Link: https://leetcode.com/problems/missing-number/
    * Purpose: Find the only number in the range that is missing from the array.
    * Parameters: int [] - a sequence of integer from o to n
    * Returns: int - a missing interger in the sequence
    * Pre-Condition: n == nums.length
                   : 1 <= n <= 104
                   : 0 <= nums[i] <= n
                   : All the numbers of nums are unique.
      Post-Condition : None
    */

    // vanilla java: runtime: O(n^2), memory: O(1)
    public static int missingNumber(int[] nums) {
        // Chack if there is any missing element
        for(int i = 0; i < nums.length; i++) {
            int num = i;
            if(!Arrays.stream(nums).anyMatch(n -> n == num)){
                return i;
            }
        }
        // if no missing element return the highest number + 1
        return Arrays.stream(nums).max().getAsInt() + 1;
    }

}
