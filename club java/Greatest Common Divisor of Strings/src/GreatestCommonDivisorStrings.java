public class GreatestCommonDivisorStrings {
    public static void main(String[] args) {
        System.out.println("\n === solution 1 === \n");
        System.out.println(gcdOfStrings_M1("ABCABC", "ABC")); // ABC
        System.out.println(gcdOfStrings_M1("ABABAB", "ABAB")); // AB
        System.out.println(gcdOfStrings_M1("LEET", "CODE")); // ""
        System.out.println(gcdOfStrings_M1("LEET", "LEETLEETLEET")); // LEET
        System.out.println(gcdOfStrings_M1("LEETLEETLEET", "LEET")); // LEET
        System.out.println(gcdOfStrings_M1("LEET", "LEETLEETLEE")); // ""
        System.out.println(gcdOfStrings_M1("ab", "ab")); // ab
        System.out.println(gcdOfStrings_M1("a", "aaaa")); // a

        System.out.println("\n === solution 2 === \n");
        System.out.println(gcdOfStrings_M2("ABCABC", "ABC")); // ABC
        System.out.println(gcdOfStrings_M2("ABABAB", "ABAB")); // AB
        System.out.println(gcdOfStrings_M2("LEET", "CODE")); // ""
        System.out.println(gcdOfStrings_M2("LEET", "LEETLEETLEET")); // LEET
        System.out.println(gcdOfStrings_M2("LEETLEETLEET", "LEET")); // LEET
        System.out.println(gcdOfStrings_M2("LEET", "LEETLEETLEE")); // ""
        System.out.println(gcdOfStrings_M2("ab", "ab")); // ab
        System.out.println(gcdOfStrings_M2("a", "aaaa")); // a
    }

    /**
     Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
     Purpose: Find the largest string x such that x divides both str1 and str2
            : two strings s and t, we say "t divides s" if and only if s = t + t + ... + t
     parameter: String str1 - String 1
              : String str2 - String 2
     return: String x - such that x divides both str1 and str2
     Pre-Condition: 1 <= str1.length, str2.length <= 1000
                  : str1 and str2 consist of English uppercase letters.
     Post-Condition: none
     **/
    // Brute Force - runtime: O(mn), memory: O(m)
    public static String gcdOfStrings_M1(String str1, String str2) {
        String smallest;
        String x = "";
        if(str1.length() > str2.length()) {
            smallest = str2;
        }else{
            smallest = str1;
        }

        for(int i = smallest.length(); i > 0; i--) { // O(min(str1, str2))
            x = smallest.substring(0, i);
            int len = x.length();
            if(str1.length() % len == 0 && str2.length() % len == 0){
                if(x.repeat(str1.length() / len).equals(str1) && x.repeat(str2.length() / len).equals(str2)) { // O(n)
                    return x;
                }
            }

        }

        return "";
    }

    /**
     Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
     Purpose: Find the largest string x such that x divides both str1 and str2
     : two strings s and t, we say "t divides s" if and only if s = t + t + ... + t
     parameter: String str1 - String 1
     : String str2 - String 2
     return: String x - such that x divides both str1 and str2
     Pre-Condition: 1 <= str1.length, str2.length <= 1000
     : str1 and str2 consist of English uppercase letters.
     Post-Condition: none
     **/
    // Brute Force - runtime: O(n), memory: O(1)
    public static String gcdOfStrings_M2(String str1, String str2) {
        int gcd = gcd(str1.length(), str2.length()); // log(n)
        if((str1 + str2).equals(str2 + str1)){ // O(n)
            return str1.substring(0, gcd);
        }else{
            return "";
        }
    }

    public static int gcd(int x, int y) {
        if(y == 0) {
            return x;
        }
        return gcd(y, x % y);
    }
}
