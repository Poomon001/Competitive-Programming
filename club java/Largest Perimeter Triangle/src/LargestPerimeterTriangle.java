import java.util.Arrays;

public class LargestPerimeterTriangle {
    public static void main(String[] args) {
        int[] nums1 = {1,2,1};
        int[] nums2 = {1,2,2};
        int[] nums3 = {3,2,3,4};
        int[] nums4 = {2,2,6,1};
        int[] nums5 = {2,2,3,11,6};

        System.out.println(largestPerimeter(nums1)); // 0
        System.out.println(largestPerimeter(nums2)); // 5
        System.out.println(largestPerimeter(nums3)); // 10
        System.out.println(largestPerimeter(nums4)); // 5
        System.out.println(largestPerimeter(nums5)); // 7
    }

    /**
     * Link: https://leetcode.com/problems/largest-perimeter-triangle/description/
     * Purpose: Find the largest perimeter of a triangle with a non-zero area. If cannot find the area, return 0.
     * Parameter: int[] nums - The array of integer
     * Returns: int - an area of the triangle
     * Pre-Condition: 3 <= nums.length <= 104
     *              : 1 <= nums[i] <= 106
     *              : area must be a + b > c
     * Post-Condition: none
     **/
    // runtime: O(nlog(n)), memory: O(1)
    public static int largestPerimeter(int[] nums) {
        Arrays.sort(nums);

        // a + b > c
        int i = nums.length -1;
        int j = nums.length -2;
        int k = nums.length -3;

        while(k >= 0){
            int a = nums[k--];
            int b = nums[j--];
            int c = nums[i--];
            if(a + b > c){
                return a + b + c;
            }
        }
        return 0;
    }
}
