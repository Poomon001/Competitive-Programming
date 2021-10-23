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
        // left and right most index
        int left = 0;
        int right = nums.length-1;

        // keep cutting a sorted part of an array (an answer will be a part that is not sorted) [4,5,6,7,0,1,2,3] -> [7,0]
        // eg. [4,5,6,7,0,1,2,3] -> [0,1,2,3] -> 0
        while(left < right){
            int middle = left + (right - left) / 2;

            // array is in a sorted order
            if(nums[left] < nums[right]){
                return nums[left];
            }

            // we divide array by 2 until the 2 last elements left
            if(right-left == 1){
                return Math.min(nums[left], nums[right]);
            }

            /** left < middle < right is sorted **/
            // sorted on left side, remove the left side
            if(nums[left] <= nums[middle] && nums[middle] > nums[right]){
                    left = middle;
                    continue;
            }

            // sorted on right side, remove the right side
            if(nums[left] > nums[middle] && nums[middle] <= nums[right]){
                right = middle;
                continue;
            }
        }

        // in case left == right, we return left or right is fine
        return nums[left];
    }
}
