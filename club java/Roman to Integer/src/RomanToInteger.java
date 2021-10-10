import java.util.Hashtable;

public class RomanToInteger {
    public static void main(String[] args) {
        System.out.println(romanToInt("III")); // 3
        System.out.println(romanToInt("IV")); // 4
        System.out.println(romanToInt("IX")); // 9
        System.out.println(romanToInt("LVIII")); // 58
        System.out.println(romanToInt("MCMXCIV")); // 1994
    }

    /**
     * Link: https://leetcode.com/problems/roman-to-integer/
     * Purpose: Convert a Roman number to Integer
     * Parameters: String s, a roman number
     * Returns: int sum - an integer
     * Pre-Condition: 1 <= s.length <= 15
     *              : s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
     *              : It is guaranteed that s is a valid roman numeral in the range [1, 3999].
     Post-Condition : None
     **/

    // run-time: O(n), memory: O(1)
    public static int romanToInt(String s) {
        // given by the question
        Hashtable <String, Integer> chart = new Hashtable<>();
        chart.put("I", 1);
        chart.put("V", 5);
        chart.put("X", 10);
        chart.put("L", 50);
        chart.put("C", 100);
        chart.put("D", 500);
        chart.put("M", 1000);

        // 1.read the string backwards
        // 2.if right value is less or equal to left, the add them together
        // 3.if right value is more than left, then subtract them
        int prevRight = chart.get(Character.toString(s.charAt(s.length() -1)));
        int sum = prevRight;
        for(int i = s.length() - 2; i >= 0; i--){
            int currLeft = chart.get(Character.toString(s.charAt(i)));
            // if right value is less or equal to left, the add them together
            if(prevRight <= currLeft){
                sum += currLeft;
            // if right value is more than left, then subtract them
            }else{
                sum -= currLeft;
            }
            prevRight = currLeft;
        }
        return sum;
    }
}
