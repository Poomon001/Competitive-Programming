import java.util.Comparator;
import java.util.PriorityQueue;

public class LastStoneWeight {
    public static void main(String[] args) {
        System.out.println(lastStoneWeight(new int[] {2,7,4,1,18})); // 4
        System.out.println(lastStoneWeight(new int[] {2,7,4,1,8,1})); // 1
        System.out.println(lastStoneWeight(new int[] {2})); // 2
        System.out.println(lastStoneWeight(new int[] {3,3})); // 0
    }

    /**
     * Link: https://leetcode.com/problems/last-stone-weight/
     * Purpose: Find the final stone weight, where:
     *        : On each turn, we choose the heaviest two stones and smash them together, leaving the remainder,
     * Parameters: int[] stones - an array of positive integers.
     * Returns: int - the final stone weight.
     * Pre-Condition: 1 <= stones.length <= 30
     *              : 1 <= stones[i] <= 1000
     * Post-Condition : None
     **/
    // max-heap: runtime: O(nlogn), memory: O(n)
    public static int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        for(Integer stone : stones) {
            maxHeap.add(stone);
        }

        while(maxHeap.size() > 1) {
            int stone_one = maxHeap.poll();
            int stone_two = maxHeap.poll();
            int remainder = stone_one - stone_two;
            if(remainder > 0) {
                maxHeap.add(remainder);
            }
        }
        return maxHeap.isEmpty() ? 0 : maxHeap.poll();
    }
}
