import java.util.HashMap;
import java.util.Stack;

public class NextGreaterElement1 {
    public static void main (String[] args){
        int[] nums1 = {4,1,2};
        int[] nums2 = {1,3,4,2};

        int[] nums3 = {2,4};
        int[] nums4 = {1,2,3,4};

        int[] nums5 = {1,3,5,2,4};
        int[] nums6 = {6,5,4,3,2,1,7};


        System.out.println("\n === Brute force solution ===\n");
        print(nextGreaterElement1_M1(nums1, nums2)); // -1 3 -1
        print(nextGreaterElement1_M1(nums3, nums4)); // 3 -1
        print(nextGreaterElement1_M1(nums5, nums6)); // 7 7 7 7 7

        System.out.println("\n === next greater element algo solution ===\n");
        print(nextGreaterElement1_M2(nums1, nums2)); // -1 3 -1
        print(nextGreaterElement1_M2(nums3, nums4)); // 3 -1
        print(nextGreaterElement1_M2(nums5, nums6)); // 7 7 7 7 7
    }

    /**
     * Link: https://leetcode.com/problems/next-greater-element-i/
     * Purpose: Find a next greater element of all elements in array nums1. Use the order of array nums2. -1 if doesn't
     *          have a next greater element
     * Parameters: int[] nums1 - an array of integers that we want to find its next greater element.
     *           : int[] nums2 - a larger array that is a super set of nums1. We need to find the next greater element
     *                           of each element in nums1 in this nums2 array.
     * Returns: int[] - a list of next greater element. -1 if dooesn't have a next greater element.
     * Pre-Condition: 1 <= nums1.length <= nums2.length <= 1000
     *              : 0 <= nums1[i], nums2[i] <= 104
     *              : All integers in nums1 and nums2 are unique.
     *              : All the integers of nums1 also appear in nums2.
     * Post-Condition : None
     **/

    // brute force - runtime: O(n^2), memory: O(1)
    public static int[] nextGreaterElement1_M1(int[] nums1, int[] nums2) {
        int[] ans = new int [nums1.length]; // returned array doesnt count towards memory
        int index = 0; // keep tack of ans index

        for(int i = 0; i < nums1.length; i++){
            // if currNum is positive that means we found a matching element in nums2
            int currNum = -1;
            for(int j = 0; j < nums2.length; j++){
                // find a matching element. Then assign a it to currNum
                if(nums1[i] == nums2[j]){
                    currNum = nums1[i];
                }

                // found a j that is greater than currNum(i), assign j to ans array
                if(currNum > -1 && nums2[j] > currNum){
                    ans[index++] = nums2[j];
                    break;
                }

                // cannot find a j that is greater than currNum(i) at the end of the loop
                if(j == nums2.length-1){
                    ans[index++] = -1;
                }
            }
        }
        return ans;
    }

    /**
     * Link: https://leetcode.com/problems/next-greater-element-i/
     * Purpose: Find a next greater element of all elements in array nums1. Use the order of array nums2. -1 if doesn't
     *          have a next greater element
     * Parameters: int[] nums1 - an array of integers that we want to find its next greater element.
     *           : int[] nums2 - a larger array that is a super set of nums1. We need to find the next greater element
     *                           of each element in nums1 in this nums2 array.
     * Returns: int[] - a list of next greater element. -1 if dooesn't have a next greater element.
     * Pre-Condition: 1 <= nums1.length <= nums2.length <= 1000
     *              : 0 <= nums1[i], nums2[i] <= 104
     *              : All integers in nums1 and nums2 are unique.
     *              : All the integers of nums1 also appear in nums2.
     * Post-Condition : None
     **/
    // A next greater element stack algo question: runtime: O(n), memory: O(n)
    // 1. find all next greater elements in a larger array using the algo
    // 2. then return only the asking next greater elements (the asking elements are all element in nums1)
    public static int[] nextGreaterElement1_M2(int[] nums1, int[] nums2) {
        // store current element and its next greater number
        HashMap<Integer, Integer> nextGreatest = new HashMap<>();
        Stack<Integer> numsStack = new Stack<>();

        // find all next greater elements in a larger array (nums2)
        for(int i = 0; i < nums2.length; i++) {
            // O(1)
            while(!numsStack.isEmpty() && numsStack.peek() < nums2[i]) {
                nextGreatest.put(numsStack.pop(), nums2[i]);
            }
            numsStack.push(nums2[i]);
        }

        // return only the answer pair that the question asked (specify on nums1)
        for(int i = 0; i < nums1.length; i++){
            // if the element has a next greater, assign the next greater. Otherwise assign -1
            if(nextGreatest.containsKey(nums1[i])){
                nums1[i] = nextGreatest.get(nums1[i]);
            }else{
                nums1[i] = -1;
            }
        }
        return nums1;
    }

    private static void print(int[] ans){
        for (int i:ans) {
            System.out.print(i + " ");
        }
        System.out.println("");
    }
}
