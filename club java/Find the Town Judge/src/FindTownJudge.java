import java.util.HashMap;
import java.util.HashSet;

public class FindTownJudge {
    public static void main(String[] args) {
        System.out.println("\n === Solution 1 === \n");
        System.out.println(findJudge_M1(2, new int[][]{{1, 2}})); // 2
        System.out.println(findJudge_M1(3, new int[][]{{1, 3}, {2, 3}})); // 3
        System.out.println(findJudge_M1(3, new int[][]{{1, 3}, {2, 3}, {3, 1}})); // -1
        System.out.println(findJudge_M1(3, new int[][]{{1, 2}, {2, 3}})); // -1

        System.out.println("\n === Solution 2 === \n");
        System.out.println(findJudge_M2(2, new int[][]{{1, 2}})); // 2
        System.out.println(findJudge_M2(3, new int[][]{{1, 3}, {2, 3}})); // 3
        System.out.println(findJudge_M2(3, new int[][]{{1, 3}, {2, 3}, {3, 1}})); // -1
        System.out.println(findJudge_M2(3, new int[][]{{1, 2}, {2, 3}})); // -1
    }

    /**
     Link: https://leetcode.com/problems/find-the-town-judge/
     Purpose: Find the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
     : If the town judge exists, then:
     1. The town judge trusts nobody.
     2. Everybody (except for the town judge) trusts the town judge.
     3. There is exactly one person that satisfies properties 1 and 2.
     parameter: int[][] trust - a list of pair [a, b] where "a" person trusts "b" person
     : int n - a town population
     return: int - The label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
     Pre-Condition: 1 <= n <= 1000
     : 0 <= trust.length <= 10^4
     : trust[i].length == 2
     : All the pairs of trust are unique.
     : a != b
     : 1 <= a, b <= n
     Post-Condition: none
     **/
    // HashSet - runtime: O(n), memory: O(n)
    public static int findJudge_M1(int n, int[][] trust) {
        // Town Judge trust nobody
        HashSet<Integer> disqualifedSet = new HashSet();
        // everyone trust town judge
        HashMap<Integer, Integer> candidateToTrusts = new HashMap<>();

        for(int[] pair: trust){
            int trusting = pair[0];
            int trusted = pair[1];
            Integer num = candidateToTrusts.getOrDefault(trusted , 0) + 1;
            disqualifedSet.add(trusting);
            candidateToTrusts.put(trusted, num);
        }

        for(int i = 1; i <= n; i ++) {
            if(!disqualifedSet.contains(i) && candidateToTrusts.getOrDefault(i, 0) == n -1) {
                return i;
            }
        }
        return -1;
    }

    /**
     Link: https://leetcode.com/problems/find-the-town-judge/
     Purpose: Find the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
     : If the town judge exists, then:
     1. The town judge trusts nobody.
     2. Everybody (except for the town judge) trusts the town judge.
     3. There is exactly one person that satisfies properties 1 and 2.
     parameter: int[][] trust - a list of pair [a, b] where "a" person trusts "b" person
     : int n - a town population
     return: int - The label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
     Pre-Condition: 1 <= n <= 1000
     : 0 <= trust.length <= 10^4
     : trust[i].length == 2
     : All the pairs of trust are unique.
     : a != b
     : 1 <= a, b <= n
     Post-Condition: none
     **/
    // Array Mapping Index - runtime: O(n), memory: O(n)
    public static int findJudge_M2(int n, int[][] trust) {
        // Town judge trust nobody
        int[] candidateToTrusting = new int[n + 1];
        // everyone trust town judge
        int[] candidateToTrusted = new int[n + 1];

        for(int[] pair: trust){
            int trusting = pair[0];
            int trusted = pair[1];
            candidateToTrusting[trusting]++;
            candidateToTrusted[trusted]++;
        }

        for(int i = 1; i <= n; i ++) {
            if(candidateToTrusting[i] == 0 && candidateToTrusted[i] == n - 1) {
                return i;
            }
        }
        return -1;
    }
}
