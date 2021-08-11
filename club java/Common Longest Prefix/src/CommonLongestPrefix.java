public class CommonLongestPrefix {
    public static void main(String[] args){
        String [] words1 = {"cir","car"}; // c
        String [] words2 = {"flower","flow","flight"}; // fl
        String [] words3 =  {"dog","racecar","car"}; // ""
        System.out.println(commonLongestPrefix(words1));
        System.out.println(commonLongestPrefix(words2));
        System.out.println(commonLongestPrefix(words3));
    } // main

    /**
     * Link: https://leetcode.com/problems/longest-common-prefix/
     * Purpose: find the longest common prefix string amongst an array of strings.
     * parameter: array - contains words
     * return: string - longest common prefix
     * Pre-Condition: only lower-case English letters.
     *              : number of words is between 1 and 200
     *              : number of chars in a word is between 0 and 200
     * Post-Condition: none
     **/
    // solution 2. Solution 1 is in python
    public static String commonLongestPrefix(String[] words){
        // input array string is empty, return "" and done
        if(words.length == 0){
            return "";
        }

        String longestPrefix = words[0];
        for(int i = 1; i < words.length; i++){
            // -1 = not contain
            // check the if two string match after each update of longestPrefix
            // repeat the loop until both string match
            while(words[i].indexOf(longestPrefix) != 0){

                // remove one last character from longestPrefix and save the new string longestPrefix
                longestPrefix = longestPrefix.substring(0, longestPrefix.length()-1);
            }
        }
        return longestPrefix;
    }
}
