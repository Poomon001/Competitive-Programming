import java.lang.*;

public class SortArrayByParityII {
    public static void main(String[] args) {
        int[] nums1 = {4,2,5,7};
        int[] nums2 = {2,3};
        int[] nums3 = {3,2};
        System.out.println(" ===\n solution M1 ===\n");
        print(sortArrayByParityII_M2(nums1)); // 4 5 2 7
        print(sortArrayByParityII_M2(nums2)); // 2 3
        print(sortArrayByParityII_M2(nums3)); // 2 3
        System.out.println(" ===\n solution M2 ===\n");
        print(sortArrayByParityII_M1(nums1)); // 4 5 2 7
        print(sortArrayByParityII_M1(nums2)); // 2 3
        print(sortArrayByParityII_M1(nums3)); // 2 3

    }

    /*
    * Link: https://leetcode.com/problems/sort-array-by-parity-ii/
    * Purpose: Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
    * Parameters: int[] - array of integer where its length is even
    * Returns: int[] - the array that has even number in even index and odd number in odd index
    * Pre-Condition: 2 <= nums.length <= 2 * 104
                   : nums.length is even.
                   : Half of the integers in nums are even.
                   : 0 <= nums[i] <= 1000
      Post-Condition : None
    */

    // creating new array: memory: O(n), runtime: O(n)
    public static int[] sortArrayByParityII_M1(int[] nums) {
        int length = nums.length;
        int[] odd = new int [length/2];
        int[] even = new int [length/2];

        int i = 0; // keep track of even index
        int j = 0; // keep track of odd index

        // separate even and odd number into 2 diff arrays
        for(int num:nums){
            if(num%2 == 0){
                even[i++] = num;
            }else{
                odd[j++] = num;
            }
        }

        // put even numbers to even indies and put odd numbers to odd indies
        i = 0;
        j = 0;
        for(int k = 0; k < length; k++){
            // even index
            if(k%2 == 0) {
                nums[k] = even[i++];
            // odd index
            }else{
                nums[k] = odd[j++];
            }
        }

        return nums;
    }

    /*
    * Link: https://leetcode.com/problems/sort-array-by-parity-ii/
    * Purpose: Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
    * Parameters: int[] - array of integer where its length is even
    * Returns: int[] - the array that has even number in even index and odd number in odd index
    * Pre-Condition: 2 <= nums.length <= 2 * 104
                   : nums.length is even.
                   : Half of the integers in nums are even.
                   : 0 <= nums[i] <= 1000
      Post-Condition : None
    */

    // in place sort: memory: O(1), runtime: O(n)
    // 1. find an even index that contains odd number
    // 2. find the front-most odd index that contain even number from nums
    // 3. use these 2 indices to swap 2 numbers
    public static int[] sortArrayByParityII_M2(int[] nums) {
        int length = nums.length;
        int i = 0; // keep track of even index
        int j = 1; // keep track of odd index

        while(i < length){
            // 1. find an even index that contain odd number
            if(nums[i]%2 == 0){
                // not our target b/c it is already correct (even num in even index)
                i += 2;

            }else{
                 // 2. find the front-most odd index that contains even number
                 while(nums[j]%2 == 1){
                     // not our target b/c it is already correct (odd num in odd index)
                     j += 2;
                 }

                // 3. use these 2 indices to swap 2 numbers
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                i += 2;
            }
        }
        return nums;
    }

    private static void print(int[] nums){
        for (int num:nums) {
            System.out.print(num + " ");
        }
        System.out.println("\n");
    }
}
