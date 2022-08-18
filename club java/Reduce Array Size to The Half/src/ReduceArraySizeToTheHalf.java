import java.util.*;
public class ReduceArraySizeToTheHalf {
    public static void main(String[] args){
        int[] nums1 = {3,3,3,3,5,5,5,2,2,7};
        int[] nums2 = {7,7,7,7,7,7};
        int[] nums3 = {1,9};
        int[] nums4 = {100,100,3,9};
        int[] nums5 = {1,2,3,4,5,6,7,8,9,10};

        System.out.println(minSetSize(nums1)); // 2 because we remove {3, 5}
        System.out.println(minSetSize(nums2)); // 1 because we remove {7}
        System.out.println(minSetSize(nums3)); // 1 because we remove {1}
        System.out.println(minSetSize(nums4)); // 1 because we remove {1}
        System.out.println(minSetSize(nums5)); // 5 because we remove {1,2,3,4,5}
    }

    /**
     * Link: https://leetcode.com/problems/reduce-array-size-to-the-half/
     * Purpose:  the minimum size of the set removed integer so that at least half of the integers of the array are removed.
     * Parameter: int[] arr - an integer array
     * Returns: int counter - the minimum size of the set removed integer
     * Pre-Condition: 2 <= arr.length <= 105
     *              : arr.length is even.
     *              : 1 <= arr[i] <= 105
     * Post-Condition: none
     **/
    // greedy and sort: runtime - O(nlon(n)), memory: O(n)
    public static int minSetSize(int[] arr){
        // {integer, occurance}
        Hashtable<Integer, Integer> map = new Hashtable();
        int size = arr.length;
        int half = (int)arr.length/2;

        // count occurance
        for(int i : arr){
            if(map.containsKey(i)){
                map.put(i, map.get(i) + 1);
            }else{
                map.put(i, 1);
            }
        }

        // convert hashtable to 2D array to sort by occurance
        int[][] arrayMap = new int[map.size()][2];
        int i = 0;
        for(Map.Entry<Integer, Integer> data: map.entrySet()){
            arrayMap[i++] = new int[]{data.getKey(), data.getValue()};
        }
        Arrays.sort(arrayMap, (a,b) -> Integer.compare(b[1], a[1]));

        int counter = 0; // number of removed integer

        // remove the most occurance integers until the size is at at least half
        for(int[] nums:arrayMap){
            if(size > half){
                size -= nums[1];
                counter++;
            }
        }

        return counter;
    }
}
