import java.util.Arrays;

public class findMaxAverage {
    public static void main(String[] args) {
        System.out.println("\n === Solution 1 === \n");
        System.out.println(findMaxAverage_M1(new int[]{1,12,-5,-6,50,3}, 4)); // 12.75
        System.out.println(findMaxAverage_M1(new int[]{1,12,-5,-6,50,3}, 2)); // 26.5
        System.out.println(findMaxAverage_M1(new int[]{-1}, 1)); // -1.0
        System.out.println(findMaxAverage_M1(new int[]{0,4,0,3,2}, 1)); // 4.0

        System.out.println("\n === Solution 2 === \n");
        System.out.println(findMaxAverage_M2(new int[]{1,12,-5,-6,50,3}, 4)); // 12.75
        System.out.println(findMaxAverage_M2(new int[]{1,12,-5,-6,50,3}, 2)); // 26.5
        System.out.println(findMaxAverage_M2(new int[]{-1}, 1)); // -1.0
        System.out.println(findMaxAverage_M2(new int[]{0,4,0,3,2}, 1)); // 4.0
    }

    /**
    * Link: https://leetcode.com/problems/maximum-average-subarray-i/
    * Purpose: Find a contiguous subarray whose length is equal to k that has the maximum average value from array nums
    * Parameters: int[] nums - a int array
    * Returns: double - a contiguous subarray whose length is equal to k that has the maximum average value
    * Pre-Condition: n == nums.length
    *              : 1 <= k <= n <= 105*
    *              : -104 <= nums[i] <= 104
    * Post-Condition : None
    */
    // window slicing - runtime: O(n*m), memory:O(1)
    public static double findMaxAverage_M1(int[] nums, int k) {
        int maxSum = Integer.MIN_VALUE;

        for(int i = 0; i <= nums.length - k; i++) {
            int sum = Arrays.stream(nums, i, i + k).sum();
            maxSum = Math.max(sum, maxSum);
        }
        return (double) maxSum / k;
    }

    /**
    * Link: https://leetcode.com/problems/maximum-average-subarray-i/
    * Purpose: Find a contiguous subarray whose length is equal to k that has the maximum average value from array nums
    * Parameters: int[] nums - a int array
    * Returns: double - a contiguous subarray whose length is equal to k that has the maximum average value
    * Pre-Condition: n == nums.length
    *              : 1 <= k <= n <= 105*
    *              : -104 <= nums[i] <= 104
    * Post-Condition : None
    */
    // window slicing - runtime: O(n), memory:O(1)
    public static double findMaxAverage_M2(int[] nums, int k) {
        int sum = Arrays.stream(nums, 0, k).sum();
        int maxSum = sum;

        for(int i = k; i < nums.length; i++) {
            int last = nums[i - k];
            int head = nums[i];
            sum = sum + head - last;
            maxSum = Math.max(sum, maxSum);
        }
        return (double) maxSum / k;
    }
}
