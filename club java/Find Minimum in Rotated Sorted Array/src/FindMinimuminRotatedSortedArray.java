public class FindMinimuminRotatedSortedArray {
    public static void main(String[] args) {
        int[] nums1 = {3,4,5,1,2};
        int[] nums2 = {4,5,6,7,0,1,2};
        int[] nums3 = {2,4,5,6,7,0,1};
        int[] nums4 = {1,2,4,5,6,7,0};
        int[] nums5 = {7,0,1,2,4,5,6};
        int[] nums6 = {11,13,15,17};
        int[] nums7 = {1,2};
        int[] nums8 = {2,1};
        System.out.println(findMin(nums1)); // 1
        System.out.println(findMin(nums2)); // 0
        System.out.println(findMin(nums3)); // 0
        System.out.println(findMin(nums4)); // 0
        System.out.println(findMin(nums5)); // 0
        System.out.println(findMin(nums6)); // 11
        System.out.println(findMin(nums7)); // 1
        System.out.println(findMin(nums8)); // 1
    }

    /**
     * Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
     * Purpose: Given a sorted array n which is rotated between 1 and n. Find the smallest element from a list of UNIQUE elements.
     *        : nums = [0,1,2,4,5,6,7]
     *        : [4,5,6,7,0,1,2] if it was rotated 4 times.
     *        : [0,1,2,4,5,6,7] if it was rotated 7 times.
     * Parameters: int[] nums - a sorted array n which is rotated (All elements are unique)
     * Returns: int - the smallest element in the array
     * Pre-Condition : n == nums.length
     *                : 1 <= n <= 5000
     *                : -5000 <= nums[i] <= 5000
     *                : All the integers of nums are unique.
     *                : nums is sorted and rotated between 1 and n times.
     * Post-Condition  : none
     * Requirment: Must use Binary Search to solve this problem
     **/
    // runtime: O(log(n)), memory: O(1)
    public static int findMin(int[] nums) {
        // If nums[mid] < nums[right], the right half [mid, right] is sorted,
        // The minimum number is in [left, mid], including mid because mid could be the lowest in the sorted
        // e.g [1, 2, 3, 4, 5] and [4, 5, 1, 2, 3]
        //
        // 2. If nums[mid] >= nums[right], the rotation range is from the left half to the mid [left, mid].
        // The minimum cannot be in the rotation range [left, mid], so the minimum so is in (mid, right].
        // e.g [3, 4, 5, 1, 2] and [2, 3, 4, 5, 1]

        int left = 0;
        int right = nums.length - 1;
        int mid = 0;
        while (left <= right) {
            mid = (right - left) / 2 + left;

            if(nums[mid] < nums[right]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return nums[mid];
    }
}
