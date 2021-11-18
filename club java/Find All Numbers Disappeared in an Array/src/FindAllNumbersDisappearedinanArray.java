import java.util.*;
public class FindAllNumbersDisappearedinanArray {
    public static void main(String[] args) {
        int[] nums1 = {4,3,2,7,8,2,3,1};
        int[] nums2 = {1,1};
        int[] nums3 = {1,2,4,3,5};
        int[] nums4 = {1,1,2,2};

        System.out.println("\n+==== Solution M1 ====+\n");
        print(findDisappearedNumbers_M1(nums1)); // [5,6]
        print(findDisappearedNumbers_M1(nums2)); // [2]
        print(findDisappearedNumbers_M1(nums3)); // []
        print(findDisappearedNumbers_M1(nums4)); // [3,4]

        System.out.println("\n+==== Solution M2 ====+\n");
        print(findDisappearedNumbers_M2(nums1)); // [5,6]
        print(findDisappearedNumbers_M2(nums2)); // [2]
        print(findDisappearedNumbers_M2(nums3)); // []
        print(findDisappearedNumbers_M2(nums4)); // [3,4]

    }

    // runtime: O(n), memory:O(n) -> answer doesnt count toward memory
    public static List<Integer> findDisappearedNumbers_M1(int[] nums) {
        List<Integer> answer = new ArrayList();

        // <unique num>
        HashSet<Integer> seen = new HashSet();

        int len = nums.length;

        // get all unique integer in num
        for(int num:nums){
            if(!seen.contains(num)){
                seen.add(num);
            }
        }

        // answer contains all numbers that is not in the unique list from [1, nums.length]
        for(int i = 1; i <= len; i++){
            if(!seen.contains(i)){
                answer.add(i);
            }
        }
        return answer;
    }

    // runtime: O(n), memory:O(1) -> answer doesnt count toward memory
    public static List<Integer> findDisappearedNumbers_M2(int[] nums) {
        Integer[] answer = new Integer[nums.length*2];

        // get [1, n] in answer array
        for(int i = 0; i < nums.length; i++){
            answer[i] = i+1;
        }

        int j = 0; // keep track of nums

        // replace a number m in the answer array with -1 if m is in the nums array
        // note: answer array contains [1, n] orderly
        while (j < nums.length){
            int kIndex = nums[j] - 1;
            answer[kIndex] = -1;
            j++;
        }

        // add non -1 to the back of the answer array (continue at nums.length)
        int k = nums.length;
        for(int i = 0; i < nums.length; i++){
            if(answer[i] != -1){
                answer[k] = answer[i];
                k++;
            }
        }

        // slice array from the part we append actually answer (nums.length to k)
        int from = nums.length;
        int to = k;
        return Arrays.asList(Arrays.copyOfRange(answer, from, to));
    }

    private static void print(List<Integer> nums){
        for(int num:nums){
            System.out.print(num+" ");
        }
        System.out.print("\n");
    }
}
