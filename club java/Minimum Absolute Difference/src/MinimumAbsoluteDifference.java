import java.util.*;
public class MinimumAbsoluteDifference {
    public static void main(String[] args){
        int[] nums1 = {4,2,1,3};
        int[] nums2 = {1,3,6,10,15};
        int[] nums3 = {4,1};
        int[] nums4 = {3,8,-10,23,19,-4,-14,27};
        int[] nums5 = {40,11,26,27,-20};

        System.out.println(minimumAbsDifference(nums1)); // [[1,2],[2,3],[3,4]]
        System.out.println(minimumAbsDifference(nums2)); // [[1,3]]
        System.out.println(minimumAbsDifference(nums3)); // [1, 4]
        System.out.println(minimumAbsDifference(nums4)); // [[-14,-10],[19,23],[23,27]]
        System.out.println(minimumAbsDifference(nums5)); // [[26,27]]
    }

    /**
     * Link: https://leetcode.com/problems/minimum-absolute-difference/
     * Purpose: Find all pairs of elements with the minimum absolute difference of any two elements in ascending order
     * Parameters: int[] arr - a list of unique integers
     * Returns: List<List<Integer>> pair - all pairs of elements with the minimum absolute difference of any two elements in ascending order
     * Pre-Condition: 2 <= arr.length <= 10^5
     *              : -10^6 <= arr[i] <= 10^6
     * Post-Condition : None
     **/

    // runtime: O(nlon(n)), memory: O(n) -> if doesnt count the answer then O(1)
    public static List<List<Integer>> minimumAbsDifference(int[] arr) {
        // the minimum different must be the current number and the next lowest higher number
        Arrays.sort(arr);

        List<List<Integer>> pair = new ArrayList();
        int prev = arr[0];
        int minDiff = arr[1] - prev;

        // find min different
        for(int i = 1; i < arr.length; i++){
            int diff = arr[i] - prev;
            minDiff = minDiff > diff? diff : minDiff;
            prev = arr[i];
        }

        // store pairs that has a min diff
        for(int i = 0; i < arr.length; i++){
            List<Integer> nums = new ArrayList();
            if(i + 1 < arr.length && arr[i+1] - arr[i] == minDiff){
                nums.add(arr[i]);
                nums.add(arr[i+1]);
                pair.add(nums);
            }
        }
        return pair;
    }
}
