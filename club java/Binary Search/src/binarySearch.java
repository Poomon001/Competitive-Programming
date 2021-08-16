public class binarySearch {
    public static void main(String[] args){
        int[] x = {1,3,5,6,10,11};
        System.out.println(searchInsert(x, 6));
    }

    /*
     * Purpose: Find the index of searching element in an array O(log(n))
     * Parameters: int[] nums - the array of number
     *             int target - the elements want to find in the array
     * Returns: int - the index of the target element in the array
     * Post-Condition: the array is in the same order
     */
    public static int searchInsert(int[] nums, int target) {
        int first = 0;
        int last = nums.length - 1;
        int middle = (last+first)/2;

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
                middle = (last+first)/2;
            }

            // target is less than the value from and include the middle to the highest value
            // then set a new highest range to middle - 1
            if(target < nums[middle]){
                last = middle - 1;
                middle = (last+first)/2;
            }
        }
        return last + 1;
    }
}
