import java.util.Arrays;

public class ThreeSumClosest {
    public static void main(String[] arg){
        int[] nums1 = {-1,2,1,-4};
        int[] nums2 = {0,0,0};
        int[] nums3 = {-1,2,1,-4, 5, 6, 3,2};
        int[] nums4 = {-1,-2,-1,-4, -5, 16, -3,-2};

        System.out.println("\n+=== Solution 1 ===+\n");
        System.out.println(threeSumClosest_m1(nums1, 1)); // 2
        System.out.println(threeSumClosest_m1(nums1, -4)); // -4
        System.out.println(threeSumClosest_m1(nums1, -10)); // -4

        System.out.println(threeSumClosest_m1(nums2, 0)); // 0
        System.out.println(threeSumClosest_m1(nums2, 10)); // 0

        System.out.println(threeSumClosest_m1(nums3, 100)); // 14
        System.out.println(threeSumClosest_m1(nums3, 5)); // 5
        System.out.println(threeSumClosest_m1(nums3, -4)); // -4

        System.out.println(threeSumClosest_m1(nums4, -12)); // -12
        System.out.println(threeSumClosest_m1(nums4, 1)); // -4
        System.out.println(threeSumClosest_m1(nums4, -15)); //-12
        System.out.println(threeSumClosest_m1(nums4, 3)); // 7
        System.out.println(threeSumClosest_m1(nums4, 4)); // 7

        System.out.println("\n+=== Solution 2 ===+\n");
        System.out.println(threeSumClosest_m2(nums1, 1)); // 2
        System.out.println(threeSumClosest_m2(nums1, -4)); // -4
        System.out.println(threeSumClosest_m2(nums1, -10)); // -4

        System.out.println(threeSumClosest_m2(nums2, 0)); // 0
        System.out.println(threeSumClosest_m2(nums2, 10)); // 0

        System.out.println(threeSumClosest_m2(nums3, 100)); // 14
        System.out.println(threeSumClosest_m2(nums3, 5)); // 5
        System.out.println(threeSumClosest_m2(nums3, -4)); // -4

        System.out.println(threeSumClosest_m2(nums4, -12)); // -12
        System.out.println(threeSumClosest_m2(nums4, 1)); // -4
        System.out.println(threeSumClosest_m2(nums4, -15)); //-12
        System.out.println(threeSumClosest_m2(nums4, 3)); // 7
        System.out.println(threeSumClosest_m2(nums4, 4)); // 7

    }

    /**
     * Link: https://leetcode.com/problems/3sum-closest/description/
     * Purpose: Find three integers in nums such that the sum is closest to target.
     * Parameter: int[] nums - The array of integer
     *          : int target - a target integer
     * Returns: int closestSum - the sum is closest to target.
     * Pre-Condition: 3 <= nums.length <= 1000
     *              : -1000 <= nums[i] <= 1000
     *              : -10^4 <= target <= 10^4
     * Post-Condition: none
     **/
    // runtime: O(n^2), memory: O(1)
    public static int threeSumClosest_m1(int[] nums, int target) {
        int closestSum = nums[0] + nums[1] + nums[2];

        Arrays.sort(nums);

        int i = 0;
        int j = 1;

        while(i < j){
            j = i + 1;
            int k = nums.length-1;
            while(j < k){
                int localSum = nums[i] + nums[j] + nums[k];

                // save the closest sum to the target
                if(Math.abs(localSum - target) < Math.abs(closestSum - target)){
                    closestSum = localSum;
                }

                // move pointer (ideal is 0)
                int diff = localSum - target;
                if(diff > 0){
                    k--;
                }else if (diff < 0){
                    j++;
                }else{
                    return closestSum;
                }
            }
            i++;
        }
        return closestSum;
    }

    /**
     * Link: https://leetcode.com/problems/3sum-closest/description/
     * Purpose: Find three integers in nums such that the sum is closest to target.
     * Parameter: int[] nums - The array of integer
     *          : int target - a target integer
     * Returns: int closestSum - the sum is closest to target.
     * Pre-Condition: 3 <= nums.length <= 1000
     *              : -1000 <= nums[i] <= 1000
     *              : -10^4 <= target <= 10^4
     * Post-Condition: none
     **/
    // runtime: O(n^3), memory: O(1)
    public static int threeSumClosest_m2(int[] nums, int target) {
        int closestSum = nums[0] + nums[1] + nums[2];
        int localSum = 0;

        for(int i = 0; i < nums.length; i++){
            int one = nums[i];
            for(int j = 0; j < nums.length; j++){
                if(i != j){
                    int two = nums[j];
                    for(int k = 0; k < nums.length; k++){
                        if(j != k && i != k){
                            int three = nums[k];
                            localSum = one + two + three;
                            if(Math.abs(localSum - target) < Math.abs(closestSum - target)){
                                closestSum = localSum;
                            }
                        }
                    }
                }
            }
        }
        return closestSum;
    }
}
