public class ReverseWords {
    public static void main(String[] args) {
        String s1 = "";
        String s2 = "hello";
        String s3 = "hello world";
        String s4 = "the sky is blue";
        String s5 = "  hello world  ";
        String s6 = "a good   example";

        System.out.println("\n === solution 1 ===\n");
        System.out.println(reverserWords_M1(s1)); // ""
        System.out.println(reverserWords_M1(s2)); // "hello"
        System.out.println(reverserWords_M1(s3)); // "world hello"
        System.out.println(reverserWords_M1(s4)); // "blue is sky the"
        System.out.println(reverserWords_M1(s5)); // "world hello"
        System.out.println(reverserWords_M1(s6)); // "example good a"

        System.out.println("\n === solution 2 ===\n");
        System.out.println(reverserWords_M2(s1)); // ""
        System.out.println(reverserWords_M2(s2)); // "hello"
        System.out.println(reverserWords_M2(s3)); // "world hello"
        System.out.println(reverserWords_M2(s4)); // "blue is sky the"
        System.out.println(reverserWords_M2(s5)); // "world hello"
        System.out.println(reverserWords_M2(s6)); // "example good a"
    }

    /**
     * Link: https://leetcode.com/problems/reverse-words-in-a-string/description/
     * Purpose: Reverse all words in a string, replace multiple spaces with one space, and remove leading and trailing spaces
     * Parameter: String s - a string
     * Returns: String ans - the expected word
     * Pre-Condition: 1 <= s.length <= 10^4
     * Post-Condition: none
     **/
    public static String reverserWords_M1(String s){
        String[] words = s.split(" ");
        String ans = "";
        for(String word:words){
            if(word != ""){
                ans = word + " " + ans;
            }
        }
        return ans.strip();
    }

    public static String reverserWords_M2(String s) {
        String[] words = s.trim().split("\\s+");
        int i = 0;
        int j = words.length - 1;
        while(i < j) {
            String temp = words[i];
            words[i] = words[j];
            words[j] = temp;
            i++;
            j--;
        }
        return String.join(" ", words);
    }
}
