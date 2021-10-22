import java.util.HashMap;
import java.lang.*;
import java.util.*;

public class SortCharactersByFrequency {
    public static void main(String[] args){
        System.out.println(frequencySort("tree")); // eert
        System.out.println(frequencySort( "cccaaa")); // aaaccc
        System.out.println(frequencySort("Aabb")); // bbAa
    }

    /**
     * Link: https://leetcode.com/problems/sort-characters-by-frequency/
     * Purpose: Sort an input string in decreasing order based on the frequency of the characters.
     * Parameters: String s - an input string
     * Returns: String answer - a sorted string by the frequency of the characters.
     * Pre-Condition: 1 <= s.length <= 5 * 105
     *              : s consists of uppercase and lowercase English letters and digits.
     * Post-Condition : None
     **/
    // runtime: O(n^2), memory: O(n)
    public static String frequencySort(String s) {
        // <alphabet, counter>
        HashMap<Character, Integer> frequency = new HashMap<>();
        String answer = "";
        for(char c : s.toCharArray()){
            if(frequency.containsKey(c)){
                // increment counter if duplicate char is found
                frequency.put(c, frequency.get(c)+1);
            }else{
                // initialize each non-duplicate char and count 1
                frequency.put(c, 1);
            }
        }

        // sort the hashmap by value and add the key to answer string n times; n = its value
        for(Character k:sortByValue(frequency).keySet()){
            for(int i = 0; i < frequency.get(k);i++){
                answer += k.toString();
            }
        }
//        printHashTable(sortByValue(frequency));
        return answer;
    }

    /**
     * Purpose: Sort an hashmap by value
     * Parameters: HashMap<Character, Integer> map - an input hashmap
     * Returns: HashMap<Character, Integer> newMap - a Sorted hashmap by value
     * Pre-Condition: none
     * Post-Condition : None
     **/
    private static HashMap<Character, Integer> sortByValue(HashMap<Character, Integer> map){
        List<Map.Entry<Character, Integer>> list = new LinkedList<>(map.entrySet());

        // sorted by value backward
        Collections.sort(list, (k1, k2) -> k2.getValue().compareTo(k1.getValue()));

        HashMap<Character, Integer> newMap = new LinkedHashMap<>();

        // put sorted value to hashmap
        for(Map.Entry<Character, Integer> ele:list){
            newMap.put(ele.getKey(), ele.getValue());
        }
        return newMap;
    }

    /**
     * Purpose: print both key and value of a hashmap
     * Parameters: HashMap<Character, Integer> map - an input hashmap
     * Returns: none
     * Pre-Condition: none
     * Post-Condition : None
     **/
    private static void printHashTable(HashMap<Character, Integer> map){
        for(Character name: map.keySet()){
            char key = (char)name;
            int value = (int)map.get(name);
            System.out.println("key: " + key + ", value: " + value);
        }
    }
}
