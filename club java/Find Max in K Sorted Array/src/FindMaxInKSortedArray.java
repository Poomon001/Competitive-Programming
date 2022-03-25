public class FindMaxInKSortedArray {
    public static void main(String[] args) {
        int[] nums1 = {1,2,3,6,10,2,1,0};
        int[] nums2 = {1,2,3,6,10};
        int[] nums3 = {2,1,0};
        int[] nums4 = {1,2,3,6,10,2,1};
        int[] nums5 = {1,2,3,10,2,1,0};
        int[] nums6 = {10};

        System.out.println(findMax(nums1)); // 10
        System.out.println(findMax(nums2)); // 10
        System.out.println(findMax(nums3)); // 2
        System.out.println(findMax(nums4)); // 10
        System.out.println(findMax(nums5)); // 10
        System.out.println(findMax(nums6)); // 10
    }

    /**
     * Purpose: Find if a maximum number in an array where index of 0th to kth is sorted in an ascending order
     *        : And index of k-1th to len(array)th is sorted in an descending order
     * Parameters: int[] n - the array specified by the question
     * Returns: int - maximun integer in the array
     * Pre-Condition: 1 <= n.length <= 2^31 - 1
     *              : 0 <= k <= n.length - 1
     * Post-Condition : none
     **/
    // runtime: O(log(n)), memory: O(1)
    public static int findMax(int[] nums){
        int left = 0;
        int right = nums.length;
        int middle = 0;

        while(left < right){
            middle = (int)(left + (right - left)/2);
            if(nums[left] >= nums[middle]){
                right = middle;
            }else{
                left = middle;
            }
        }
        return nums[middle];
    }

}
