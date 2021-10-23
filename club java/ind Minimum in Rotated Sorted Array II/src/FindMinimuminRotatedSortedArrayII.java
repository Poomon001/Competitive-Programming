public class FindMinimuminRotatedSortedArrayII {
    public static void main(String[] args) {
        int[] nums1 = {1,3,5};
        int[] nums2 = {5,1,3};
        int[] nums3 = {3,5,1};
        int[] nums4 = {2,2,2,0,1};
        int[] nums5 = {1,2,2,2,0};
        int[] nums6 = {0,1,2,2,2};
        int[] nums7 = {2,0,1,2,2};
        int[] nums8 = {2,2,0,1,2,2};
        int[] nums9 = {2,2,2,0,1,2};
        int[] nums10 = {2,2,2,0,1,1,1,2};
        int[] nums11 = {2,4,5,6,7,0,1};
        int[] nums12 = {10,1,10,10,10};
        int[] nums13 = {1,1,0,1,1,1,1,1,1,1,1,1};
        int[] nums14 = {1,1,1,1,1,1,1,1,1,1,1,1};

        System.out.println(findMin(nums1)); // 1
        System.out.println(findMin(nums2)); // 1
        System.out.println(findMin(nums3)); // 1
        System.out.println(findMin(nums4)); // 0
        System.out.println(findMin(nums5)); // 0
        System.out.println(findMin(nums6)); // 0
        System.out.println(findMin(nums7)); // 0
        System.out.println(findMin(nums8)); // 0
        System.out.println(findMin(nums9)); // 0
        System.out.println(findMin(nums10)); // 0
        System.out.println(findMin(nums11)); // 0
        System.out.println(findMin(nums12)); // 1
        System.out.println(findMin(nums13)); // 0
        System.out.println(findMin(nums14)); // 1
    }

    /**
     * Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
     * Purpose: Given a sorted array n which is rotated between 1 and n. Find the smallest element from a list of DUPLICATED elements.
     *        : nums = [0,1,2,4,5,6,7]
     *        : [4,5,6,7,0,1,2] if it was rotated 4 times.
     *        : [0,1,2,4,5,6,7] if it was rotated 7 times.
     * Parameters: int[] nums - a sorted array n which is rotated (May contain Duplicated elements)
     * Returns: int - the smallest element in the array
     * Pre-Condition : n == nums.length
     *               : 1 <= n <= 5000
     *               : -5000 <= nums[i] <= 5000
     *               : nums is sorted and rotated between 1 and n times.
     * Post-Condition  : none
     * Requirment: Must use Binary Search to solve this problem
     **/
    // runtime (best / average / worse): O(log(n)) / O(log(n)) / O(n), memory: O(1)
    public static int findMin(int[] nums) {
        // pointer to left and right most indices
        int left = 0;
        int right = nums.length-1;

        // remove the sorted part
        while(left < right){
            int middle = left + (right-left)/2;

            // this is already sorted
            if(nums[left] < nums[right]){
                return nums[left];
            }

            // we divide array by 2 until the 2 last elements left
            if(right-left == 1){
                return Math.min(nums[left], nums[right]);
            }

            /** sorted: left < middle < right **/
            // sorted on left side, remove the left side
            if(nums[left] <= nums[middle] && nums[middle] > nums[right]){
                left = middle;
                continue;
            }

            // sorted on right side, remove the right side
            if(nums[left] > nums[middle] && nums[middle] <= nums[right]){
                right =  middle;
                continue;
            }

            // left, mid, right ele are the same number, so we ignore left and right but keep mid
            if(nums[left] == nums[middle] && nums[middle] == nums[right]){
               right = right-1;
               left = left+1;
            }
        }

        // in case left == right, we return left or right is fine
        return nums[left];
    }
}
