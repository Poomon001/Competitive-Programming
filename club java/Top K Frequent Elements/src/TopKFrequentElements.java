import java.util.*;
public class TopKFrequentElements {
    public static void main(String[] args){
        int[] nums1 = {1,1,1,2,2,3};
        int[] nums2 = {3,3,3,1,2,2};
        int[] nums3 = {3,3,3,2,1,1};
        int[] nums4 = {1};
        int[] nums5 = {1,2,3,4,5,6,7,8,1,1,2,2,1,2,3,3,3,3,3,4,6,7,2,2,7,7,7,7,7,7,7};

        System.out.println("\n === Solution 1 === \n");
        System.out.println(Arrays.toString(topKFrequent_M1(nums1, 2))); // [1, 2]
        System.out.println(Arrays.toString(topKFrequent_M1(nums2, 2))); // [3, 2]
        System.out.println(Arrays.toString(topKFrequent_M1(nums3, 2))); // [3, 1]
        System.out.println(Arrays.toString(topKFrequent_M1(nums4, 1))); // [1]
        System.out.println(Arrays.toString(topKFrequent_M1(nums5, 2))); // [7, 2]
        System.out.println(Arrays.toString(topKFrequent_M1(nums5, 3))); // [7, 2, 3]
        System.out.println(Arrays.toString(topKFrequent_M1(nums5, 4))); // [7, 2, 3, 1]

        System.out.println("\n === Solution 2 === \n");
        System.out.println(Arrays.toString(topKFrequent_M2(nums1, 2))); // [1, 2]
        System.out.println(Arrays.toString(topKFrequent_M2(nums2, 2))); // [3, 2]
        System.out.println(Arrays.toString(topKFrequent_M2(nums3, 2))); // [3, 1]
        System.out.println(Arrays.toString(topKFrequent_M2(nums4, 1))); // [1]
        System.out.println(Arrays.toString(topKFrequent_M2(nums5, 2))); // [7, 2]
        System.out.println(Arrays.toString(topKFrequent_M2(nums5, 3))); // [7, 2, 3]
        System.out.println(Arrays.toString(topKFrequent_M2(nums5, 4))); // [7, 2, 3, 1]
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
    public static int[] topKFrequent_M1(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> numTofreq = new HashMap<>();
        for (int n : nums) {
            numTofreq.put(n, numTofreq.getOrDefault(n, 0) + 1);
        }

        // Sort entries by frequency descending
        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(numTofreq.entrySet());
        entries.sort((a, b) -> Integer.compare(b.getValue(), a.getValue()));

        // Collect top k keys
        int[] ans = new int[k];
        for (int i = 0; i < k && i < entries.size(); i++) {
            ans[i] = entries.get(i).getKey();
        }
        return ans;
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
    // runtime: O(nlog(k)), memory: O(n) -> where n is unique number and log(k) is the height of heap size k
    public static int[] topKFrequent_M2(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> numTofreq = new HashMap<>();
        for (int n : nums) {
            numTofreq.put(n, numTofreq.getOrDefault(n, 0) + 1);
        }

        // Min-heap: int[]{count, num}
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        for (Map.Entry<Integer, Integer> entry : numTofreq.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            if (heap.size() < k) {
                heap.add(new int[]{count, num});
            } else if (count > heap.peek()[0]) { // compare to smallest in heap
                heap.poll();
                heap.add(new int[]{count, num});
            }
        }

        // Collect top k keys
        int[] res = new int[k];
        for (int i = res.length - 1; i >= 0; i--) {
            res[i] = heap.poll()[1];
        }
        return res;
    }
}
