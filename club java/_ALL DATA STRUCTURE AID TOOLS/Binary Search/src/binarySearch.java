public class binarySearch {
    public static void main(String[] args){
        System.out.println("\n === Set 1 ===\n");
        int[] x = {1,3,5,6,10,11};
        System.out.println(searchInsert(x, 6)); // 3
        System.out.println(searchInsert(x, 10)); // 4
        System.out.println(searchInsert(x, 1)); // 0
        System.out.println(searchInsert(x, 11)); // 5
        System.out.println(searchInsert(x, 9)); // -1

        System.out.println("\n === Set 2 ===\n");
        int[] y = {20, 30, 40, 50, 100};
        System.out.println(searchInsert(y, 20)); // 0
        System.out.println(searchInsert(y, 30)); // 1
        System.out.println(searchInsert(y, 50)); // 3
        System.out.println(searchInsert(y, 100)); // 4
        System.out.println(searchInsert(y, 9)); // -1
    }

    /*
     * Purpose: Find the index of searching element in an array O(log(n))
     * Parameters: int[] nums - the array of number
     *             int target - the elements want to find in the array
     * Returns: int - the index of the target element in the array
     * Post-Condition: the array is in the same order
     */

    // since it is sorted from 1 to half, use binary search
    // binary search - runtime: O(log(n)), memory: O(1)
    public static int searchInsert(int[] nums, int target) {
        int first = 0;
        int last = nums.length - 1;
        int middle = first + (last - first) / 2;

        // loop until the target is found or the not found (when last < first)
        while(last>=first){

            // find target and return index
            if(target == nums[middle]){
                return middle;
            }

            // target is greater than the value from the lowest to and include middle value
            // then set a new lowest range to middle + 1
            if(target > nums[middle]){
                first = middle + 1;
                middle = first + (last - first) / 2;
            }

            // target is less than the value from and include the middle to the highest value
            // then set a new highest range to middle - 1
            if(target < nums[middle]){
                last = middle - 1;
                middle = first + (last - first) / 2;
            }
        }
        return -1;
    }
}
