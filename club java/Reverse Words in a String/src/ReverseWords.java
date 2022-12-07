public class ReverseWords {
    public static void main(String[] args) {
        String s1 = "";
        String s2 = "hello";
        String s3 = "hello world";
        String s4 = "the sky is blue";
        String s5 = "  hello world  ";
        String s6 = "a good   example";
        System.out.println(reverserWords(s1)); // ""
        System.out.println(reverserWords(s2)); // "hello"
        System.out.println(reverserWords(s3)); // "world hello"
        System.out.println(reverserWords(s4)); // "blue is sky the"
        System.out.println(reverserWords(s5)); // "world hello"
        System.out.println(reverserWords(s6)); // "example good a"
    }

    /**
     * Link: https://leetcode.com/problems/reverse-words-in-a-string/description/
     * Purpose: Reverse all words in a string, replace multiple spaces with one space, and remove leading and trailing spaces
     * Parameter: String s - a string
     * Returns: String ans - the expected word
     * Pre-Condition: 1 <= s.length <= 10^4
     * Post-Condition: none
     **/
    public static String reverserWords(String s){
        String[] words = s.split(" ");
        String ans = "";
        for(String word:words){
            if(word != ""){
                ans = word + " " + ans;
            }
        }
        return ans.strip();
    }
}
