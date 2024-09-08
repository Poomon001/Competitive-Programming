import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

public class DivideArrayInSetsConsecutiveNumbers {
    public static void main(String[] args) {
        int[] stress = new int[200000];
        for(int i = 0; i < 200000; i++){
            stress[i] = (i % 2) + 1;
        }
        System.out.println("\n === solution 1 === \n");
        System.out.println(isPossibleDivide_M1(new int[]{1,2,3,3,4,4,5,6}, 3)); // false
        System.out.println(isPossibleDivide_M1(new int[]{1,2,3,3,4,4,5,6}, 4)); // true
        System.out.println(isPossibleDivide_M1(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 3)); // true
        System.out.println(isPossibleDivide_M1(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 4)); // false
        System.out.println(isPossibleDivide_M1(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 1)); // true
        System.out.println(isPossibleDivide_M1(new int[]{1,2,3,4}, 1)); // true
        System.out.println(isPossibleDivide_M1(new int[]{1,2,3,4}, 2)); // true
        System.out.println(isPossibleDivide_M1(new int[]{1,2,3,4}, 4)); // true
        System.out.println(isPossibleDivide_M1(stress, 2)); // true -> may take a few seconds

        System.out.println("\n === solution 2 === \n");
        System.out.println(isPossibleDivide_M2(new int[]{1,2,3,3,4,4,5,6}, 3)); // false
        System.out.println(isPossibleDivide_M2(new int[]{1,2,3,3,4,4,5,6}, 4)); // true
        System.out.println(isPossibleDivide_M2(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 3)); // true
        System.out.println(isPossibleDivide_M2(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 4)); // false
        System.out.println(isPossibleDivide_M2(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 1)); // true
        System.out.println(isPossibleDivide_M2(new int[]{1,2,3,4}, 1)); // true
        System.out.println(isPossibleDivide_M2(new int[]{1,2,3,4}, 2)); // true
        System.out.println(isPossibleDivide_M2(new int[]{1,2,3,4}, 4)); // true
        System.out.println(isPossibleDivide_M2(stress, 2)); // true

        System.out.println("\n === solution 3 === \n");
        System.out.println(isPossibleDivide_M3(new int[]{1,2,3,3,4,4,5,6}, 3)); // false
        System.out.println(isPossibleDivide_M3(new int[]{1,2,3,3,4,4,5,6}, 4)); // true
        System.out.println(isPossibleDivide_M3(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 3)); // true
        System.out.println(isPossibleDivide_M3(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 4)); // false
        System.out.println(isPossibleDivide_M3(new int[]{3,2,1,2,3,4,3,4,5,9,10,11}, 1)); // true
        System.out.println(isPossibleDivide_M3(new int[]{1,2,3,4}, 1)); // true
        System.out.println(isPossibleDivide_M3(new int[]{1,2,3,4}, 2)); // true
        System.out.println(isPossibleDivide_M3(new int[]{1,2,3,4}, 4)); // true
        System.out.println(isPossibleDivide_M3(stress, 2)); // true
    }

    /**
     Link: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
     Purpose: Determine whether it is possible to divide the nums array into sets of k consecutive numbers.
     parameter: int[] nums - array of integers
     : int k - an integer
     return: boolean - true if it is possible. Otherwise, return false
     Pre-Condition: 1 <= k <= nums.length <= 105
     : 1 <= nums[i] <= 109
     Post-Condition: none
     **/
    // If the smallest number in the possible-to-split array is V, then numbers V+1, V+2, ... V+k-1 must contain there as well.
    // Brute force - runtime: O(n^2), memory: O(n)
    public static boolean isPossibleDivide_M1(int[] nums, int k){
        int len = nums.length;
        if(len % k != 0) return false;

        Integer[] numsBoxed = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(numsBoxed));
        while(numbers.size() > 0){ // O(n/k group)
            int smallest = Collections.min(numbers); // O(n)
            for(int i = smallest; i < smallest + k; i++){ // O(k)
                if(numbers.contains(i)){ // O(n)
                    numbers.remove(Integer.valueOf(i)); // O(n)
                }else{
                    return false;
                }
            }
        }

        return true;
    }

    /**
     Link: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
     Purpose: Determine whether it is possible to divide the nums array into sets of k consecutive numbers.
     parameter: int[] nums - array of integers
     : int k - an integer
     return: boolean - true if it is possible. Otherwise, return false
     Pre-Condition: 1 <= k <= nums.length <= 105
     : 1 <= nums[i] <= 109
     Post-Condition: none
     **/
    // If the smallest number in the possible-to-split array is V, then numbers V+1, V+2, ... V+k-1 must contain there as well.
    // HashMap - runtime: O(n^2/k), memory: O(n)
    public static boolean isPossibleDivide_M2(int[] nums, int k) {
        int len = nums.length;
        if(len % k != 0) return false;

        HashMap<Integer, Integer> numbersToFreq = new HashMap<>();
        for(Integer num : nums) {
            numbersToFreq.put(num, numbersToFreq.getOrDefault(num, 0) + 1);
        }

        while(numbersToFreq.size() > 0){ // O(n/k group)
            int smallest = Collections.min(numbersToFreq.keySet()); // O(n)
            for(int i = smallest; i < smallest + k; i++){ // O(k)
                if(numbersToFreq.containsKey(i)){
                    numbersToFreq.put(i, numbersToFreq.get(i) - 1);
                    if(numbersToFreq.get(i) == 0) {
                        numbersToFreq.remove(i); // O(1)
                    }
                }else{
                    return false;
                }
            }
        }

        return true;
    }

    /**
     Link: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
     Purpose: Determine whether it is possible to divide the nums array into sets of k consecutive numbers.
     parameter: int[] nums - array of integers
              : int k - an integer
     return: boolean - true if it is possible. Otherwise, return false
     Pre-Condition: 1 <= k <= nums.length <= 105
                  : 1 <= nums[i] <= 109
     Post-Condition: none
     **/
    // If the smallest number in the possible-to-split array is V, then numbers V+1, V+2, ... V+k-1 must contain there as well.
    // HashMap and sort - runtime: O(nlogn), memory: O(n)
    public static boolean isPossibleDivide_M3(int[] nums, int k){
        int len = nums.length;
        if(len % k != 0) return false;

        HashMap<Integer, Integer> numbersToFreq = new HashMap<>();
        for(Integer num : nums) {
            numbersToFreq.put(num, numbersToFreq.getOrDefault(num, 0) + 1);
        }
        Arrays.sort(nums); // O(nlogn)

        // O(n) b/c the first if statement ensure that used number cannot enter (e.g nums = [1,2,3,4,5,6], k = 3)
        for(int num:nums) {
            if(numbersToFreq.getOrDefault(num, 0) > 0) { // if smallest num is ran out, skip to the next number
                for(int i = num; i < num + k; i++) {
                    if(numbersToFreq.getOrDefault(i, 0) > 0) {
                        numbersToFreq.put(i, numbersToFreq.get(i) - 1);
                    }else{
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
