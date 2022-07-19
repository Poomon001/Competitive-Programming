import java.util.*;
public class PascalTriangle {
    public static void main(String[] args){
        System.out.println(generate(1));
        System.out.println(generate(2));
        System.out.println(generate(3));
        System.out.println(generate(4));
        System.out.println(generate(5));

    }

    /**
    * Link: https://leetcode.com/problems/pascals-triangle/
    * Purpose: Find all the numRows of Pascal's triangle.
    * Parameter: int numRows - The number of row in Pascal's triangle
    * Returns: List<List<Integer>> answer - All the numRows of Pascal's triangle
    * Pre-Condition: 1 <= numRows <= 30
    * Post-Condition: none
    **/
    // run-time: O(n^2), memory: O(1)
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> answer = new ArrayList();

        for(int i = 0; i < numRows; i++){
            List<Integer> row = new ArrayList();
            for(int j = 0; j <= i; j++){
                if(j == 0 || j == i){
                    row.add(1);
                }else{
                    row.add(answer.get(i-1).get(j-1) + answer.get(i-1).get(j));
                }
            }
            answer.add(row);
        }
        return answer;
    }
}
