public class MaximumRepeatingSubstring {
    public static void main(String[] args){
        System.out.println(maxRepeating("ababc", "ab")); // 2
        System.out.println(maxRepeating("ababc", "ba")); // 1
        System.out.println(maxRepeating("ababc", "ac")); // 0
        System.out.println(maxRepeating("a", "a")); // 1
        System.out.println(maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba")); // 5
    }

    /**
     * Link: https://leetcode.com/problems/maximum-repeating-substring/
     * Purpose: Find the maximum number of k-concatenated word in sequence
     * Parameter: String sequence - a string
     *          : String word - word pattern
     * Returns: int counter -  the maximum number of k-concatenated word in sequence
     * Pre-Condition: 1 <= sequence.length <= 100
     *              : 1 <= word.length <= 100
     *              : sequence and word contains only lowercase English letters.
     * Post-Condition: none
     **/

    // runtime: O(n^2), memory: O(1)
    public static int maxRepeating(String sequence, String word) {
        int counter = 0;
        String pattern = word;
        while(true) {
            if (sequence.contains(word)) {
                counter++;
            }else{
                break;
            }
            word += pattern;
        }
        return counter;
    }
}