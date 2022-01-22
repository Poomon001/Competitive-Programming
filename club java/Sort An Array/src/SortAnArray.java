public class SortAnArray {
    /**
     * Link: https://leetcode.com/problems/sort-an-array/
     * Purpose: Sorted an array
     * Parameters: int[] nums - an array of integer
     * Returns: int[] nums - a sorted array of integer
     * Pre-Condition: 1 <= nums.length <= 5 * 10^4
     *              : -5 * 10^4 <= nums[i] <= 5 * 10^4
     * Post-Condition : none
     **/
    public static void main(String[] args) {
        int[] nums1 = {5,1,1,2,0,8,9,0};
        int[] nums2 = {64,25,12,22,11,-10};

        for(int i:selectionSort(nums1)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:selectionSort(nums2)){
            System.out.print(i + " ");
        }
        System.out.println("");
    }

    private static void swap(int i, int j, int[] nums){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    /**
     * 1. find a lowest number in an unsorted section
     * 2. put the lowest number to the back of sorted section
     * 3. keep repeat step 1 and 2 until it covers the whole array (nums.length times)
     * **/
    // run-time: O(n^2), memory: O(1)
    public static int[] selectionSort(int[] nums){
        // keep track of sorting list
        int i = 0;
        // keep track of unsorting list
        int j = 0;
        // keep track of lowest number in a list
        int k = 0;

        // sort the whole array
        while(i < nums.length) {
            j = i;
            k = i;

            // find the lowest number in unsorted list
            while (j < nums.length) {
                if (nums[j] < nums[k]) {
                    k = j;
                }
                j++;
            }

            // swap the lowest number to the back of sorted array
            swap(i++, k, nums);
        }

        return nums;
    }
}
