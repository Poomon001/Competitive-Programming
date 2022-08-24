import java.util.Random;
public class QuickSelect {
    /**
     * Purpose: Find an Kth smallest element in an array
     * Parameters: int[] S - an array of integer
     *           : int k - an Kth smallest element
     * Returns: int - a integer of Kth smallest element
     * Pre-Condition: 1 <= nums.length <= 5 * 10^4
     *              : -5 * 10^4 <= nums[i] <= 5 * 10^4
     * Post-Condition : none
     **/

    // best: O(n), average: O(nlog(n)), worst: O(n^2)
    public static int QS(int[] S, int k){
        // catch an array with one element
        if (S.length==1)
            return S[0];

        return quickSelect(0,S.length-1,S,k);

    }

    private static int quickSelect(int left,int right, int[] array, int k){
        int kIndex = k -1;

        // divide into left and right partitions. And return Kth position of a random middle pivot (pIndex)
        // note: all left element are less, and all right element are more than array[pIndex].
        int pIndex = partition(left, right, array);

        if(kIndex < pIndex) {
            // call on left
            return quickSelect(left, pIndex - 1, array, k);
        }else if(kIndex > pIndex) {
            // call on right
            return quickSelect(pIndex + 1, right, array, k);
        }else{
            // partition middle point is at Kth index, return final answer
            return array[kIndex];
        }
    }

    /***
     * Purpose: divide array into left and right side, seperated by a pivot element. And find the Kth position of the pivot.
     * Parameters: int left - left-most index bound
     *           : int right - right-most index bound
     *           : int[] array - an array of integer
     * return: int - a Kth position of the povit element
     *
     * ***/

    private static int partition(int left, int right, int[] array){
        int pivotIndex = left;
        int pivot = array[pivotIndex];
        left = pivotIndex+1;

        // stop when left index cross right index
        while(left <= right) {
            while (left < array.length && array[left] <= pivot) {
                left++;
            }

            while (right > 0 && array[right] > pivot) {
                right--;
            }

            // stop when left index cross right index
            if (left <= right) {
                swap(array, left, right);
            }
        }
        swap(array, right, pivotIndex);

        return right; // Kth index pf pivot
    }

    private static void swap(int[]array, int a, int b){
        int tmp = array[a];
        array[a] = array[b];
        array[b] = tmp;
    }

    public static void main (String[] args){
        int[] nums0 = {5,3,2,1,6,4};
        int[] nums1 = {5,1,1,2,0,8,9,0};
        int[] nums2 = {3,9,8,4};
        int[] nums3 = {64,25,12,22,11,-10};
        int[] nums4 = {0};

        System.out.println(QS(nums0,3)); // 3
        System.out.println(QS(nums1,3)); // 1
        System.out.println(QS(nums1, 5)); // 2

        System.out.println(QS(nums2,2)); // 4
        System.out.println(QS(nums2,4)); // 9
        System.out.println(QS(nums3,2)); // 11
        System.out.println(QS(nums4,1)); // 0
    }
}

