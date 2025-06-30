import java.util.HashMap;
import java.util.Map;

public class MaximumXORofBinary {
    public static void main(String[] args) {
        System.out.println(getMaximum("11001100", "01011111")); // 11110011
        System.out.println(getMaximum("1111", "0000")); // 1111
        System.out.println(getMaximum("00000000", "11111111")); // 11111111
        System.out.println(getMaximum("11110000", "11110000")); // 11111111
        System.out.println(getMaximum("11111", "11111")); // 00000
        System.out.println(getMaximum("1100", "1010")); // 1111
    }

    /*
    * Link: IBM questions
    * Purpose: Given two binary, a currentKey and rotatedKey of equal length, rotate rotatedKey such that
    *        : The XOR of currentKey and new RotatedKey yield the maximum value.
    * Parameters: String currentKey - a string representing a fixed binary.
    *           : String rotatedKey - a string representing a rotated binary.
    * Returns: String ans - the maximum binary representing XOR of currentKey and rotatedKey
    * Pre-Condition: Only '0' and '1' are guaranteed
                   : currentKey.length() == rotatedKey.length()
                   : 1 <= currentKey.length(), rotatedKey.length() <= 10^6
      Post-Condition : None
    */
    // hashset - runtime: O(n), memory:O(1)
    public static String getMaximum(String currentKey, String rotatedKey) {
        String ans = "";
        Map<Character, Integer> keyBitToFreq = new HashMap<>();
        for (Character bit : rotatedKey.toCharArray()) {
            int count = keyBitToFreq.getOrDefault(bit, 0) + 1;
            keyBitToFreq.put(bit, count);
        }

        for (Character bit : currentKey.toCharArray()) {
            if (bit == '0' && keyBitToFreq.getOrDefault('1', 0) > 0) {
                keyBitToFreq.put('1', keyBitToFreq.get('1') - 1);
                ans += "1";
            } else if (bit == '1' && keyBitToFreq.getOrDefault('0', 0) > 0) {
                keyBitToFreq.put('0', keyBitToFreq.get('0') - 1);
                ans += "1";
            } else {
                ans += "0";
            }
        }
        return ans;
    }
}
