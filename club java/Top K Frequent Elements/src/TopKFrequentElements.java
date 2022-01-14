import java.util.*;
public class TopKFrequentElements {
    public static void main(String[] args){
        int[] nums1 = {1,1,1,2,2,3};
        int[] nums2 = {3,3,3,1,2,2};
        int[] nums3 = {3,3,3,2,1,1};
        int[] nums4 = {1};
        int[] nums5 = {1,2,3,4,5,6,7,8,1,1,2,2,1,2,3,3,3,3,3,4,6,7,2,2,7,7,7,7,7,7,7};

        for(int i:topKFrequent(nums1, 2)){
            System.out.print(i + " "); // 1 2
        }
        System.out.println("");

        for(int i:topKFrequent(nums2, 2)){
            System.out.print(i + " "); // 3 2
        }
        System.out.println("");

        for(int i:topKFrequent(nums3, 2)){
            System.out.print(i + " "); // 3 1
        }
        System.out.println("");

        for(int i:topKFrequent(nums4, 1)){
            System.out.print(i + " "); // 1
        }
        System.out.println("");

        for(int i:topKFrequent(nums5, 2)){
            System.out.print(i + " "); // 7 2
        }
        System.out.println("");

        for(int i:topKFrequent(nums5, 3)){
            System.out.print(i + " "); // 7 2 3
        }
        System.out.println("");

        for(int i:topKFrequent(nums5, 4)){
            System.out.print(i + " "); // 7 2 3 1
        }
    }

    /**
     * Link: https://leetcode.com/problems/top-k-frequent-elements/
     * Purpose: Find the k most frequent elements.
     * Parameters: int[] nums: an array of integer
     *           : int k - an integer
     * Returns: int[] ans - an array of the k most frequent elements.
     * Pre-Condition: 1 <= nums.length <= 10^5
     *              : k is in the range [1, the number of unique elements in the array].
     *              : It is guaranteed that the answer is unique.
     * Post-Condition : None
     **/
    // runtime: O(nlog(n)), memory: O(n)
    public static int[] topKFrequent(int[] nums, int k) {
        // {number, count}
        HashMap<Integer, Integer> count = new HashMap();
        int[] ans = new int[k];

        for(int i = 0; i < nums.length; i++){
            if(count.containsKey(nums[i])){
                count.put(nums[i], count.get(nums[i]) + 1);
            }else{
                count.put(nums[i], 1);
            }
        }

        // sort by values
        int[][] sortedCount = new int[count.size()][2];
        int j = 0;
        for(Map.Entry<Integer, Integer>data:count.entrySet()){
            int key = data.getKey();
            int value = data.getValue();
            sortedCount[j][0] = key;
            sortedCount[j][1] = value;
            j++;
        }
        Arrays.sort(sortedCount, (a, b) -> Integer.compare(b[1], a[1]));
//        Arrays.sort(sortedCount,  (a, b) -> {
//            System.out.println(Integer.compare(b[1], a[1]));
//            return Integer.compare(b[1], a[1]);
//        });

        // get k answers
        for(int i = 0; i < k; i++){
            ans[i] = sortedCount[i][0];
        }

        return ans;
    }
}
