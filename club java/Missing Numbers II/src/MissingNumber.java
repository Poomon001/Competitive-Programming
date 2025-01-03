import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class MissingNumber {
    public static void main(String[] args) {
        int[] nums1 = {3,0,1};
        int[] nums2 = {0,1};
        int[] nums3 = {9,6,4,2,3,5,7,0,1};

        System.out.println("\n === Solution 1 === \n");
        System.out.println(missingNumber_M1(nums1)); // 2
        System.out.println(missingNumber_M1(nums2)); // 2
        System.out.println(missingNumber_M1(nums3)); // 8

        System.out.println("\n === Solution 2 === \n");
        System.out.println(missingNumber_M2(nums1)); // 2
        System.out.println(missingNumber_M2(nums2)); // 2
        System.out.println(missingNumber_M2(nums3)); // 8

        System.out.println("\n === Solution 3 === \n");
        System.out.println(missingNumber_M3(nums1)); // 2
        System.out.println(missingNumber_M3(nums2)); // 2
        System.out.println(missingNumber_M3(nums3)); // 8

        System.out.println("\n === Solution 4 === \n");
        System.out.println(missingNumber_M4(nums1)); // 2
        System.out.println(missingNumber_M4(nums2)); // 2
        System.out.println(missingNumber_M4(nums3)); // 8
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
    public static int missingNumber_M2(int[] nums) {
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

    // sequential sum: runtime: O(n), memory: O(1)
    public static int missingNumber_M3(int[] nums) {
        int actualSum = 0;
        int expectedSum = (nums.length * (nums.length + 1)) / 2;

        for(int n:nums){
            actualSum += n;
        }

        return expectedSum - actualSum;
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

    // binary search (optimize version of M1): runtime: O(nlogn), memory: O(1)
    public static int missingNumber_M4(int[] nums) {
        // binary search: sort nums then each num will corespond to its index
        // so all numbers after the missing number will has more value than its index
        // we always keep scoping the solution by searching until left <= right

        Arrays.sort(nums);
        int left = 0;
        int right = nums.length - 1;

        // The loop continues until left exceeds right.
        // At this point, left will be positioned at the first index where the index does not match the value
        while(left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == mid) {
                // all numbers from the left up to mid are in their correct positions
                left = mid + 1;
            } else {
                // the missing number is at mid or to the left of mid.
                right = mid - 1;
            }
        }

        return left;
    }

}
