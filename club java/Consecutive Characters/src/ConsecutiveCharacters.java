public class ConsecutiveCharacters {
    public static void main(String[] args){
        System.out.println(maxPower("leetcode")); // 2
        System.out.println(maxPower("abbcccddddeeeeedcba")); // 5
        System.out.println(maxPower("triplepillooooow")); // 5
        System.out.println(maxPower("hooraaaaaaaaaaay")); // 11
        System.out.println(maxPower("tourist")); // 1
        System.out.println(maxPower("a")); // 1
        System.out.println(maxPower("aa")); // 2
        System.out.println(maxPower("aaa")); // 3
    }

    /**
     * Link: https://leetcode.com/problems/consecutive-characters/
     * Purpose: Find the maximum length of a continuous duplicated char in a string
     * Parameters: String s: a string
     * Returns: int maxDup: a maximum length of a continous duplicated char
     * Pre-Condition: 0 <= x <= 231 - 1
     * Post-Condition : 1 <= s.length <= 500
     *                : s consists of only lowercase English letters.
     **/
    // runtime: O(n), memory: O(1)
    public static int maxPower(String s) {
        char prevChar = s.charAt(0);
        int maxDup = 1;
        int dup = 1;

        // count duplicate adjcent subarray
        for(int i = 1; i < s.length(); i++){
            if(prevChar == s.charAt(i)){
                dup++;
            }else{
                dup = 1;
                prevChar = s.charAt(i);
            }
            maxDup = dup > maxDup? dup:maxDup;
        }

        return maxDup;
    }
}
