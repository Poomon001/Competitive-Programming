import java.util.*;
public class PartitionLabels {
    public static void main (String[] args){
        for(int i: partitionLabels("ababcbacadefegdehijhklij")){
            System.out.print(i + " "); // 9 7 8
        }
        System.out.println("");
        for(int i: partitionLabels("abfabcbacadefegdehijhklij")){
            System.out.print(i + " "); // 17 8
        }
        System.out.println("");
        for(int i: partitionLabels("abzabcbacadefegdehijhklij")){
            System.out.print(i + " "); // 10 7 8
        }
        System.out.println("");
        for(int i: partitionLabels("a")){
            System.out.print(i + " "); // 1
        }
        System.out.println("");
        for(int i: partitionLabels("aaaa")){
            System.out.print(i + " "); // 4
        }
        System.out.println("");
        for(int i: partitionLabels("eccbbbbdec")){
            System.out.print(i + " "); // 10
        }
        System.out.println("");
        for(int i: partitionLabels("abcdefghijklmnopqrstuvwxyz")){
            System.out.print(i + " "); // 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        }

    }

    /**
     * Link: https://leetcode.com/problems/partition-labels/
     * Purpose:  Find a list of integers representing the size of these parts.
     *        : We want to partition the string into as many parts as possible so that each letter appears in at most one part.
     * Parameters: String s - a string
     * Returns: List<Integer> ans - return a list of integers representing the size of these parts.
     * Pre-Condition: 1 <= s.length <= 500
     *              : s consists of lowercase English letters.
     * Post-Condition : none
     **/
    // runtime: O(n), space: O(1)
    public static List<Integer> partitionLabels(String s) {
        List<Integer> ans = new ArrayList();
        HashMap<Character, Integer>dic = new HashMap<>();

        // store the last position of each char
        for(int i = 0; i < s.length(); i++){
            dic.put(s.charAt(i), i);
        }

        // init the first ranges
        int start = 0;
        int end = dic.get(s.charAt(start));

        for(int i = 0; i < s.length(); i++){
            // if find a further end (within the current end range), make it new end.
            // eg: "abcab", end1 (a) = 3. But within the range of 3, end2 (b) = 4. So new end = 4
            if(end < dic.get(s.charAt(i))){
                end = dic.get(s.charAt(i));
            }

            // close the range
            if(i == end){
                ans.add(end - start + 1);
                start = end + 1;
            }
        }
        return ans;
    }
}
