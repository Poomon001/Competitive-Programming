import java.util.Arrays;
import java.util.*;
public class IsSubArray {
    public static void main(String[] args){
        // test cases
        int[] a0 = {1,2,3,4,5,6};
        int[] a1 = {1,2,3,4,5,6};
        int[] a2 = {2,1,5};
        int[] a3 = {1,5,6,7};
        int[] a4 = {1,3, 7, 6,5};
        int[] a5 = {3,4,5,6};
        int[] a6 = {1, 3, 7};
        int[] a7 = {1,2,3};

        System.out.println(isSubArray_S1(a1 ,a0)); // True
        System.out.println(isSubArray_S1(a1 ,a2)); // True
        System.out.println(isSubArray_S1(a4 ,a2)); // False
        System.out.println(isSubArray_S1(a1 ,a3)); // False
        System.out.println(isSubArray_S1(a1 ,a4)); // False
        System.out.println(isSubArray_S1(a1 ,a5)); // True
        System.out.println(isSubArray_S1(a1 ,a6)); // False
        System.out.println(isSubArray_S1(a1 ,a7)); // True
        System.out.println(isSubArray_S1(a2 ,a3)); // False
        System.out.println(isSubArray_S1(a5 ,a6)); // False

        System.out.println("\n=== method 2 ===\n");

        System.out.println(isSubArray_S2(a1 ,a0)); // True
        System.out.println(isSubArray_S2(a1 ,a2)); // True
        System.out.println(isSubArray_S2(a4 ,a2)); // False
        System.out.println(isSubArray_S2(a1 ,a3)); // False
        System.out.println(isSubArray_S2(a1 ,a4)); // False
        System.out.println(isSubArray_S2(a1 ,a5)); // True
        System.out.println(isSubArray_S2(a1 ,a6)); // False
        System.out.println(isSubArray_S2(a1 ,a7)); // True
        System.out.println(isSubArray_S2(a2 ,a3)); // False
        System.out.println(isSubArray_S2(a5 ,a6)); // False

        System.out.println("\n=== method 3 ===\n");

        System.out.println(isSubArray_S3(a1 ,a0)); // True
        System.out.println(isSubArray_S3(a1 ,a2)); // True
        System.out.println(isSubArray_S3(a4 ,a2)); // False
        System.out.println(isSubArray_S3(a1 ,a3)); // False
        System.out.println(isSubArray_S3(a1 ,a4)); // False
        System.out.println(isSubArray_S3(a1 ,a5)); // True
        System.out.println(isSubArray_S3(a1 ,a6)); // False
        System.out.println(isSubArray_S3(a1 ,a7)); // True
        System.out.println(isSubArray_S3(a2 ,a3)); // False
        System.out.println(isSubArray_S3(a5 ,a6)); // False
    }

    /*
     * Purpose: Determine if a2 a subset of a1
     * Parameters: int[] a1 - the first array of integers
     *           : int[] a2 - the second array of integers
     * Returns: boolean - true if a2 is a subset of a1 otherwise, false otherwise.
     * Pre-conditions: a1 and a2 are not empty
     *                 a1.length >= a2.length
     * Post-condition: None
     */
    /** solution 1: brute force runtime: O(n^2) + memory: O(1) **/
    public static boolean isSubArray_S1(int[] a1, int[] a2){
        boolean found = false;
        for(int i = 0; i < a2.length;i++){
            for(int j = 0; j < a1.length;j++){
                // a2 elem matches one of a1 elem, found is true
                if(a1[j] == a2[i]){
                    found = true;
                    break;
                }
            }
            // if found then continue, otherwise return false
            if(found){
                found = false;
            }else{
                return false;
            }
        }

        // found all a2 elem in a1
        return true;
    }

    /*
     * Purpose: Determine if a2 a subset of a1
     * Parameters: int[] a1 - the first array of integers
     *           : int[] a2 - the second array of integers
     * Returns: boolean - true if a2 is a subset of a1 otherwise, false otherwise.
     * Pre-conditions: a1 and a2 are not empty
     *                 a1.length >= a2.length
     * Post-condition: None
     */
    /** solution 2: sort and count: runtime: O(n*lon(n)) + memory: O(1) **/
    public static boolean isSubArray_S2(int[] a1, int[] a2){
        Arrays.sort(a1);
        Arrays.sort(a2);

        int counter = 0;
        int j = 0;

        // count 1 when a1 elem matches a2 elem
        for(int i = 0; i < a1.length;i++){
            // a2 reaches the end in the previous iteration
            if(j == a2.length){
                break;
            }
            if(a1[i] == a2[j]){
                j++;
                counter++;
            }
        }

        // all elements in a2 match elementa in a1 then a2 is a subset of a1
        if(counter == a2.length){
            return true;
        }else{
            return false;
        }
    }

    /*
     * Purpose: Determine if a2 a subset of a1
     * Parameters: int[] a1 - the first array of integers
     *           : int[] a2 - the second array of integers
     * Returns: boolean - true if a2 is a subset of a1 otherwise, false otherwise.
     * Pre-conditions: a1 and a2 are not empty
     *                 a1.length >= a2.length
     * Post-condition: None
     */
    /** solution 3: set: runtime: O(n), memory: O(n+m) **/
    public static boolean isSubArray_S3(int[] a1, int[] a2){
        Set<Integer> set = new HashSet<>();
        for(int num : a1){
            set.add(num);
        }

        for(int num : a2){
            set.add(num);
        }

        // set will remove all the duplicate number
        // if the length of the set is same as the a1.length
        // this mean all a2 elem are duplicate with a1 elem, so a2 is a subset of a1
        if(set.size() == a1.length){
            return true;
        }else {
            return false;
        }
    }
}
