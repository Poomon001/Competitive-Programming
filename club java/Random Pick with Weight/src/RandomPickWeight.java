import java.util.ArrayList;
import java.util.Arrays;

/*
    * Link: https://leetcode.com/problems/random-pick-with-weight/
    * Purpose: Implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive).
    *        : Given array of positive integers w where w[i] describes the weight of the i-th index.
    * Parameters: None
    * Returns: None
    * Pre-Condition: 1 <= w.length <= 10^4
                   : 1 <= w[i] <= 10^5
                   : pickIndex will be called at most 10^4 times.
      Post-Condition : Must complete within O(1) runtime
*/
public class RandomPickWeight {
    ArrayList<Integer> weightedRange;
    int total;
    public RandomPickWeight(int[] w) {
        // [0, 1, 4, 10] -> [[0, 1], (1, 4], (4, 10]]
        this.weightedRange = new ArrayList<>();
        this.total = 0;
        this.weightedRange.add(total);
        for(Integer i : w) {
            this.total += i;
            this.weightedRange.add(total);
        }
    }

    // runtime: O(log(n)), space: O(n)
    public int pickIndex() {
        int random = (int) (Math.random() * this.total);

        int left = 0;
        int right = this.weightedRange.size() - 1;

        while(left <= right) {
            int mid = (int)(right - left) / 2 + left;
            if(mid == 0) return 0;
            if(this.weightedRange.get(mid - 1) <= random && random < this.weightedRange.get(mid)) {
                return mid - 1; // we remove the first added 0-index
            }
            if(random > this.weightedRange.get(mid - 1)) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        int[] weights = {1, 3, 6}; // probabilities: ~10%, ~30%, ~60%
        RandomPickWeight picker = new RandomPickWeight(weights);

        int trials = 10000;
        int[] count = new int[weights.length];
        for (int i = 0; i < trials; i++) {
            int index = picker.pickIndex();
            count[index]++;
        }

        // Print result
        System.out.println("Weights: " + Arrays.toString(weights));
        System.out.println("Total trials: " + trials);
        for (int i = 0; i < weights.length; i++) {
            double percentage = (count[i] * 100.0) / trials;
            System.out.printf("Index %d picked %d times (%.2f%%)\n", i, count[i], percentage);
        }
    }
}
