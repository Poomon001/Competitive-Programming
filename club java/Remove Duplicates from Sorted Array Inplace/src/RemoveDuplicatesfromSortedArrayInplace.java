public class RemoveDuplicatesfromSortedArrayInplace {
    public static void main(String[] args) {
        int[] nums1 = {1,2,3,4,5,6,7,8,9,10};
        int[] nums2 = {1};
        int[] nums3 = {1,2};
        int[] nums4 = {1,1,2};
        int[] nums5 = {1,1,2,2};
        int[] nums6 = {1,2,2,2};
        int[] nums7 = {0,0,1,1,1,2,2,3,3,4};
        int[] nums8 = {1,1,1,1,1,1,1};

        System.out.println(removeDuplicates(nums1)); // 10
        System.out.println(removeDuplicates(nums2)); // 1
        System.out.println(removeDuplicates(nums3)); // 2
        System.out.println(removeDuplicates(nums4)); // 2
        System.out.println(removeDuplicates(nums5)); // 2
        System.out.println(removeDuplicates(nums6)); // 2
        System.out.println(removeDuplicates(nums7)); // 5
        System.out.println(removeDuplicates(nums8)); // 1
    }

    /**
     * Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
     * Purpose: 1. Find a number of unique integer in a SORTED array.
     *        : 2. Arrange so that one of each unique integers listed orderly in the array
     *        : eg [0,0,1,1,1,2,2,3,3,4]  => return 5 and array after is [0, 1, 2, 3, 4, _, _, _, _, _, _]
     * Parameters: int[] nums - an integer array
     * Returns: int counter - a number of all unique integers
     * Pre-Condition : 1 <= nums.length <= 3 * 10^4
     *               : -100 <= nums[i] <= 100
     *               : nums is sorted in non-decreasing order.
     * Post-Condition  : should NOT allocate extra space: O(1) is only accepted
     *                 : time complexity of this method should be linear: O(n) is only accepted
     *                 : should return nums array such that one of each unique integers listed orderly in the array
     **/
    // runtime: O(n), memory: O(1)
    public static int removeDuplicates(int[] nums) {
        int fIndex = 0;
        int bIndex = 1;
        int counter = 1;

        while(bIndex < nums.length){
            if(nums[fIndex] != nums[bIndex]){
                fIndex++;
                counter++;
                nums[fIndex] = nums[bIndex];
            }

            bIndex++;
        }
        return counter;
    }
}
