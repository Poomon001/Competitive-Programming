public class TargetSum {
    public static void main(String[] args) {
        int[] nums1 = {-20, 10, 20, 30, 35, 40, 60, 70};
        int[] nums2 = {-20, 0, 1, 2 ,3, 5, 10, 19, 1000};

        System.out.println("\n+=== Brute force solution ===+\n");
        for(int i:targetSum_M1(nums1, 60)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M1(nums1, 20)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M1(nums1, -10)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M1(nums2, -20)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M1(nums2, 1)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M1(nums2, 1001)){
            System.out.print(i + " ");
        }
        System.out.println("");

        System.out.println("\n+=== two pointers solution ===+\n");
        for(int i:targetSum_M2(nums1, 60)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M2(nums1, 20)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M2(nums1, -10)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M2(nums2, -20)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M2(nums2, 1)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:targetSum_M2(nums2, 1001)){
            System.out.print(i + " ");
        }
        System.out.println("");
    }

    /**
     * Link: UVic CSC 226: warm up question
     * Purpose: Determine two integer in an array that sums to a target
     * Parameters: int[] nums - an array of integer
     *           : int target - a target number
     * Returns: int[] ans - an answer pair
     * Pre-Condition: nums array is in a sorted asscending order
     *              : nums array must contain a solution
     * Post-Condition : none
     **/
    // brute force: runtime: O(n^2), memory: O(1)
    public static int[] targetSum_M1(int[] nums, int target){
        int[] ans = new int[2];

        // get the first element
        for(int i = 0; i < nums.length; i++){
            int x = nums[i];
            // get second element
            for(int j = i + 1; j < nums.length; j++){
                int y = nums[j];

                // find answer then return
                if(x + y == target){
                    ans[0] = x;
                    ans[1] = y;
                    return ans;
                }
            }
        }
        return ans;
    }

    /**
     * Link: UVic CSC 226: warm up question
     * Purpose: Determine two integer in an array that sums to a target
     * Parameters: int[] nums - an array of integer
     *           : int target - a target number
     * Returns: int[] ans - an answer pair
     * Pre-Condition: nums array is in a sorted asscending order
     *              : nums array must contain a solution
     * Post-Condition : none
     **/
    // two pointers: runtime: O(n), memory: O(1)
    public static int[] targetSum_M2(int[] nums, int target){
        int[] ans = new int[2];
        int front = 0;
        int back = nums.length -1;

        // find the target
        while(front != back){
            int currSum = nums[front] + nums[back];

            // currSum is greater than the target, we need to decrease the sum
            if(currSum > target){
               back--;
            }

            // currSum is  less than the target, we need to increase the sum
            if(currSum < target){
                front++;
            }

            // if currSum is equal to target, we return the ans
            if(currSum == target){
                ans[0] = nums[front];
                ans[1] = nums[back];
                return ans;
            }
        }
        return ans;
    }
}
