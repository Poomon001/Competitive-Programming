import java.util.HashMap;

public class ContainsDuplicateII {
    public static void main(String[] args) {
        int[] n1 = {1,2,3,1};
        int[] n2 = {1,0,1,1};
        int[] n3 = {1,2,3,1,2,3};
        int[] n4 = {99, 99};
        System.out.println("\n === optimized memory solution === \n");
        System.out.println(containsNearbyDuplicate_M1(n1, 3)); // true
        System.out.println(containsNearbyDuplicate_M1(n2, 1)); // true
        System.out.println(containsNearbyDuplicate_M1(n3, 2)); // false
        System.out.println(containsNearbyDuplicate_M1(n4, 2)); // true
        System.out.println(containsNearbyDuplicate_M1(n4, 1)); // true

        System.out.println("\n === optimized runtime solution === \n");
        System.out.println(containsNearbyDuplicate_M2(n1, 3)); // true
        System.out.println(containsNearbyDuplicate_M2(n2, 1)); // true
        System.out.println(containsNearbyDuplicate_M2(n3, 2)); // false
        System.out.println(containsNearbyDuplicate_M2(n4, 2)); // true
        System.out.println(containsNearbyDuplicate_M2(n4, 1)); // true
    }

    /**
     * Link: https://leetcode.com/problems/contains-duplicate-ii/
     * Purpose: Find if an array contain any duplicate in a range of [the current index i, to index i+k]
     * Parameters: int[] nums - an array of int
     *           : int k - a given range
     * Returns: boolean - true if conatains a duplicate in a range of [the current index i, to index i+k]. Otherwise false
     * Pre-Condition: 1 <= nums.length <= 105
     *              : -109 <= nums[i] <= 109
     *              : 0 <= k <= 105
     * Post-Condition : None
     **/
    // Optimized memory solution - runtime: O(n^2), memory: O(1)
    public static boolean containsNearbyDuplicate_M1(int[] nums, int k) {
        int i = 0;
        while(i+1 < nums.length){
            // compare current element to all elements from the next index (i+1) to index (i+k)
            for(int j = i+1; j <= i+k; j++) {
                // if any element in the range [i+1 to k] equal to the curr element
                if (nums[i] == nums[j]) {
                    return true;
                }

                // if exceed the length
                if(j == nums.length-1){
                    break;
                }
            }
            i++;
        }
        return false;
    }

    /**
     * Link: https://leetcode.com/problems/contains-duplicate-ii/
     * Purpose: Find if an array contain any duplicate in a range of [the current index i, to index i+k]
     * Parameters: int[] nums - an array of int
     *           : int k - a given range
     * Returns: boolean - true if conatains a duplicate in a range of [the current index i, to index i+k]. Otherwise false
     * Pre-Condition: 1 <= nums.length <= 105
     *              : -109 <= nums[i] <= 109
     *              : 0 <= k <= 105
     * Post-Condition : None
     **/
    // Optimized runtime solution - runtime: O(n), memory: O(n)
    public static boolean containsNearbyDuplicate_M2(int[] nums, int k) {
        // {num, index that is found}
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            // if the map already contain the num
            // And the old num's index and the current num's index are within the k range
            if(map.containsKey(nums[i]) && i - map.get(nums[i]) <= k){
                return true;
            }
            // update map: key = num and value = index
            map.put(nums[i], i);
            }
        return false;
    }
}
