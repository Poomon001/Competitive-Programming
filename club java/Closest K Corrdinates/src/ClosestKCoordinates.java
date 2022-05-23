import java.util.*;

import static java.lang.Math.*;

public class ClosestKCoordinates {
    public static void main (String[] args) {
        int[] coordinate1 = {0, 0};
        int[][] targetList1 = {{1, 2}, {2, 1}, {3, 5}, {1, 1}, {1, 0}};
        int k1 = 3;

        int[] coordinate2 = {10, 10};
        int[][] targetList2 = {{12, 12}, {22, 1}, {3, 15}, {1, 1}, {1, 0}};
        int k2 = 5;

        System.out.println("+=== Test case1 ===+");
        for(ArrayList<Object> curr:closestKCoordinates(coordinate1, targetList1, k1)){
            double distance = (double) curr.get(0);
            int x = (Integer) curr.get(1);
            int y = (Integer) curr.get(2);
            System.out.println("(" + distance + "), " + "(" + x + "," + y + ")");
        }

        System.out.println("\n+=== Test case2 ===+");
        for(ArrayList<Object> curr:closestKCoordinates(coordinate2, targetList2, k2)){
            double distance = (double) curr.get(0);
            int x = (Integer) curr.get(1);
            int y = (Integer) curr.get(2);
            System.out.println("(" + distance + "), " + "(" + x + "," + y + ")");
        }

    }

    /**
     * Purpose:  Find the closest k coordinates to the started coordinate from a list of target coordinates
     * Parameters: int[] coordinate - a coordinate
     *           : int[][] targetList
     *           : int k - an integer
     * Returns: List<ArrayList<Object>> - distance and a list of closest k ordinates to the start coordinate
     * Pre-Condition: 0 <= k <= targetList.size()
     *              : targetList.size() > 0
     * Post-Condition : none
     **/
    // runtime: O(nlog(n)), memory: O(4n) = O(n)
    public static ArrayList<ArrayList<Object>> closestKCoordinates(int[] coordinate, int[][] targetList, int k){
        ArrayList<ArrayList<Object>> array = new ArrayList();

        for(int[] target:  targetList){
            // {Double distance, {int, int} targetList}
            ArrayList<Object> curr = new ArrayList();

            // find distance
            double distance = distance(coordinate, target);

            // add distance
            curr.add(distance);

            // add coordinate
            curr.add(target[0]);
            curr.add(target[1]);

            array.add(curr);
        }

        // sort by zero index
        Collections.sort(array, (a,b) -> Double.compare((double)a.get(0), (double)b.get(0)));

        return new ArrayList(array.subList(0, k));
    }

    public static double distance(int[] coordinate, int[] other){
        int x1 = coordinate[0];
        int y1 = coordinate[1];
        int x2 = other[0];
        int y2 = other[1];
        return Math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
    }
}
