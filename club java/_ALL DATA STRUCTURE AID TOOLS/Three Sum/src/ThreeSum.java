import java.util.*;
public class ThreeSum {
    public static void main(String[] args) {
        System.out.println("\n+=== brute force solution ===+\n");
        int[] nums1 = {-1, 0, 1, 2, -1, -4};
        int[] nums2 = {};
        int[] nums3 = {1,2,3,0,-1,-2,-3,-4};
        int[] nums4 = {0};

        for (List<Integer> list : threeSum_M1(nums1)) {
            formater(list); // [-1, -1, 2] [-1, 0, 1]
        }
        System.out.println("");

        for (List<Integer> list : threeSum_M1(nums2)) {
            formater(list); // []
        }
        System.out.println("");

        for (List<Integer> list : threeSum_M1(nums3)) {
            formater(list); // [-2, -1, 3] [-4, 1, 3] [-3, 1, 2] [-3, 0, 3] [-2, 0, 2] [-1, 0, 1]
        }
        System.out.println("");

        for (List<Integer> list : threeSum_M1(nums4)) {
            formater(list); // []
        }
        System.out.println("");

        System.out.println("\n+=== sorting solution ===+\n");
        int[] nums5 = {-1, 0, 1, 2, -1, -4};
        int[] nums6 = {};
        int[] nums7 = {1,2,3,0,-1,-2,-3,-4};
        int[] nums8 = {0};

        for (List<Integer> list : threeSum_M1(nums5)) {
            formater(list); // [-1, -1, 2] [-1, 0, 1]
        }
        System.out.println("");

        for (List<Integer> list : threeSum_M2(nums6)) {
            formater(list); // []
        }
        System.out.println("");

        for (List<Integer> list : threeSum_M2(nums7)) {
            formater(list); // [-2, -1, 3] [-4, 1, 3] [-3, 1, 2] [-3, 0, 3] [-2, 0, 2] [-1, 0, 1]
        }
        System.out.println("");

        for (List<Integer> list : threeSum_M2(nums8)) {
            formater(list); // []
        }
        System.out.println("");
    }

    // format
    private static void formater(List<Integer> list){
        System.out.print("[");
        for(int i = 0; i < list.size(); i++){
            String s = i == list.size()-1?"":", ";
            System.out.print(list.get(i) + s);
        }
        System.out.print("] ");
    }

    /**
     * Link: https://leetcode.com/problems/3sum/
     * Purpose: Find all the triplets [nums[i], nums[j], nums[k]] such that
     *        : i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
     * Parameters: int[] nums - an array of integer
     * Returns: List<List<Integer>> - the triplets [nums[i], nums[j], nums[k]]
     * Pre-Condition: 0 <= nums.length <= 3000
     *              : -10^5 <= nums[i] <= 10^5
     * Post-Condition : none
     **/
    // brute force -  runtime: O(n^3), memory: O(1)
    public static List<List<Integer>> threeSum_M1(int[] nums) {
        // to get rid of duplicates
        Set<List<Integer>> setAnswer = new HashSet();

        Arrays.sort(nums); // O(nlog(n))

        for(int  i = 0; i < nums.length; i++){
            int num1 = nums[i];
            for(int j = i+1; j < nums.length; j++){
                int num2 = nums[j];
                for(int k = j+1; k < nums.length; k++){
                    int num3 = nums[k];
                    if(num1 + num2 + num3 == 0){
                        Integer[] list = {num1, num2, num3};
                        // Arrays.sort(list); // don't need this because all elements are already sorted
                        setAnswer.add(Arrays.asList(list));
                    }
                }
            }
        }
        return new ArrayList(setAnswer);
    }

    /**
     * Link: https://leetcode.com/problems/3sum/
     * Purpose: Find all the triplets [nums[i], nums[j], nums[k]] such that
     *        : i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
     * Parameters: int[] nums - an array of integer
     * Returns: List<List<Integer>> - the triplets [nums[i], nums[j], nums[k]]
     * Pre-Condition: 0 <= nums.length <= 3000
     *              : -10^5 <= nums[i] <= 10^5
     * Post-Condition : none
     **/
    // sorting solution - runtime: O(n^2), memory: O(1)
    public static List<List<Integer>> threeSum_M2(int[] nums) {
        // to get rid of duplicates
        Set<List<Integer>> setAnswer = new HashSet();

        // pointers of num1, num2, and num3
        int pNum1 = 0;

        Arrays.sort(nums); // O(nlog(n))

        while(pNum1 < nums.length){
            int pNum2 = pNum1 + 1; // 1 index after pNum1
            int pNum3 = nums.length - 1; // at the end
            int num1 = nums[pNum1];

            while(pNum2 < pNum3){
                int num2 = nums[pNum2];
                int num3 = nums[pNum3];

                if(num1 + num2 + num3 > 0){
                    pNum3--;
                }else if(num1 + num2 + num3 < 0){
                    pNum2++;
                }else{
                    Integer[] list = {num1, num2, num3};
                    // Arrays.sort(list); // don't need this because all elements are already sorted
                    setAnswer.add(Arrays.asList(list));
                    pNum2++;
                    pNum3--;
                }
            }
            pNum1++;
        }
        return new ArrayList(setAnswer);
    }
}
