import java.util.Arrays;
import java.util.Hashtable;
import java.util.Map;
import java.util.stream.IntStream;

public class SetMismatch {
    public static void main(String[] args) {
        int[] nums1 = {1,2,2,4};
        int[] nums2 = {1,1};
        int[] nums3 = {1,1,3,4,5};
        int[] nums4 = {1,2,2,3,4,5,6};
        int[] nums5 = {2,3,4,4};
        int[] nums6 = {2,1,2,4,3,5,6};
        int[] nums7 = {5,4,3,1,1};

        System.out.println("\n === solution 1 ===\n");
        print(findErrorNums_M1(nums1)); // 2 3
        print(findErrorNums_M1(nums2)); // 1 2
        print(findErrorNums_M1(nums3)); // 1 2
        print(findErrorNums_M1(nums4)); // 2 7
        print(findErrorNums_M1(nums5)); // 4 1
        print(findErrorNums_M1(nums6)); // 2 7
        print(findErrorNums_M1(nums7)); // 1 2

        System.out.println("\n === solution 2 ===\n");
        print(findErrorNums_M2(nums1)); // 2 3
        print(findErrorNums_M2(nums2)); // 1 2
        print(findErrorNums_M2(nums3)); // 1 2
        print(findErrorNums_M2(nums4)); // 2 7
        print(findErrorNums_M2(nums5)); // 4 1
        print(findErrorNums_M2(nums6)); // 2 7
        print(findErrorNums_M2(nums7)); // 1 2

        System.out.println("\n === solution 3 ===\n");
        print(findErrorNums_M3(nums1)); // 2 3
        print(findErrorNums_M3(nums2)); // 1 2
        print(findErrorNums_M3(nums3)); // 1 2
        print(findErrorNums_M3(nums4)); // 2 7
        print(findErrorNums_M3(nums5)); // 4 1
        print(findErrorNums_M3(nums6)); // 2 7
        print(findErrorNums_M3(nums7)); // 1 2

    }

    /**
     * Link: https://leetcode.com/problems/set-mismatch
     * Purpose: Find the number that occurs twice and the number that is missing from an array of 1 to n.
     * Parameter: int[] nums - an integer array of 1 to n with only 1 missing and 1 duplicate numbers
     * Returns: int[] ans -  ans[0] is the duplicate, and ans[1] is the missing
     * Pre-Condition: There is only 1 missing and 1 duplicate integers.
     *              : 2 <= nums.length <= 10^4
     *              : 1 <= nums[i] <= 10^4
     * Post-Condition: none
     **/
    // naive sort - runtime: O(nlon(n)), memory(O(1))
    public static int[] findErrorNums_M1(int[] nums) {
        Arrays.sort(nums);
        int duplicate = 0;
        int missing = 0;
        int i = 1;
        int j = 0;

        while(i < nums.length) {
            // check duplicate
            if(nums[i] == nums[j]) {
                duplicate = nums[i];

                // check missing
            } else if(nums[i] != nums[j]+1){
                missing = nums[j]+1;
            }
            i++;
            j++;
        }

        // missing the last number (n)
        if(missing == 0) {
            missing = nums.length;
        }

        // missing the first number (1)
        if(nums[0] != 1) {
            missing = 1;
        }
        return new int[]{duplicate, missing};
    }

    /**
     * Link: https://leetcode.com/problems/set-mismatch
     * Purpose: Find the number that occurs twice and the number that is missing from an array of 1 to n.
     * Parameter: int[] nums - an integer array of 1 to n with only 1 missing and 1 duplicate numbers
     * Returns: int[] ans -  ans[0] is the duplicate, and ans[1] is the missing
     * Pre-Condition: There is only 1 missing and 1 duplicate integers.
     *              : 2 <= nums.length <= 10^4
     *              : 1 <= nums[i] <= 10^4
     * Post-Condition: none
     **/
    // sort - runtime: O(nlon(n)), memory(O(1))
    public static int[] findErrorNums_M2(int[] nums) {
        Arrays.sort(nums);
        int duplicate = 0;
        int missing = 0;
        int i = 1;
        int j = 0;

        while(i < nums.length) {
            // check duplicate
            if(nums[i] == nums[j]) {
                duplicate = nums[i];
            }
            i++;
            j++;
        }

        missing = IntStream.rangeClosed(1, nums.length).sum() - (Arrays.stream(nums).sum() - duplicate);
        return new int[]{duplicate, missing};
    }

    /**
     * Link: https://leetcode.com/problems/set-mismatch
     * Purpose: Find the number that occurs twice and the number that is missing from an array of 1 to n.
     * Parameter: int[] nums - an integer array of 1 to n with only 1 missing and 1 duplicate numbers
     * Returns: int[] ans -  ans[0] is the duplicate, and ans[1] is the missing
     * Pre-Condition: There is only 1 missing and 1 duplicate integers.
     *              : 2 <= nums.length <= 10^4
     *              : 1 <= nums[i] <= 10^4
     * Post-Condition: none
     **/
    // hashtable - runtime: O(n), memory(O(n))
    public static int[] findErrorNums_M3(int[] nums) {
        Hashtable<Integer, Integer> numToCount = new Hashtable<>();
        int[] ans = new int[2];
        for(int i = 1; i < nums.length + 1; i++){
            numToCount.put(i, 0);
        }

        for(Integer num:nums) {
            numToCount.put(num, numToCount.get(num) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : numToCount.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();

            if(value == 0) {
                ans[1] = key;
            }

            if(value > 1) {
                ans[0] = key;
            }
        }

        return ans;
    }

    public static void print(int[] nums) {
        for(int ans: nums) {
            System.out.print(ans + " ");
        }
        System.out.println("");
    }
}
