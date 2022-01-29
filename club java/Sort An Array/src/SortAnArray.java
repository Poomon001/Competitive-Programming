public class SortAnArray {
    /**
     * Link: https://leetcode.com/problems/sort-an-array/
     * Purpose: Sorted an array
     * Parameters: int[] nums - an array of integer
     * Returns: int[] nums - a sorted array of integer
     * Pre-Condition: 1 <= nums.length <= 5 * 10^4
     *              : -5 * 10^4 <= nums[i] <= 5 * 10^4
     * Post-Condition : none
     **/
    public static void main(String[] args) {
        System.out.println("\n+=== quick sort ===+\n");
        int[] nums1 = {5,1,1,2,0,8,9,0};
        int[] nums2 = {64,25,12,22,11,-10};
        int[] nums3 = {0};

        for(int i:selectionSort(nums1)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:selectionSort(nums2)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:selectionSort(nums3)){
            System.out.print(i + " ");
        }
        System.out.println("");

        System.out.println("\n+=== bubble sort ===+\n");
        int[] nums4 = {5,1,1,2,0,8,9,0};
        int[] nums5 = {64,25,12,22,11,-10};
        int[] nums6 = {0};

        for(int i:bubbleSort(nums4)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:bubbleSort(nums5)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:bubbleSort(nums6)){
            System.out.print(i + " ");
        }
        System.out.println("");


        System.out.println("\n+=== insertion sort ===+\n");
        int[] nums7 = {5,1,1,2,0,8,9,0};
        int[] nums8 = {64,25,12,22,11,-10};
        int[] nums9 = {0};

        for(int i:insertionSort(nums7)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:insertionSort(nums8)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:insertionSort(nums9)){
            System.out.print(i + " ");
        }
        System.out.println("");

        System.out.println("\n+=== quick sort ===+\n");
        int[] nums10 = {5,1,1,2,0,8,9,0};
        int[] nums11 = {3,9,8,4};
        int[] nums12 = {64,25,12,22,11,-10};
        int[] nums13 = {64,25,12,22,11,-10, 78};
        int[] nums14 = {0};

        for(int i:quickSort(nums10, 0, nums10.length-1)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:quickSort(nums11, 0, nums11.length-1)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:quickSort(nums12, 0, nums12.length-1)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:quickSort(nums13, 0, nums13.length-1)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:quickSort(nums14, 0, nums14.length-1)){
            System.out.print(i + " ");
        }
        System.out.println("");

    }

    private static void swap(int i, int j, int[] nums){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    /**
     * 1. find a lowest number in an unsorted section
     * 2. queue the lowest number to the back of sorted section
     * 3. keep repeat step 1 and 2 until it covers the whole array (nums.length times)
     * **/
    // run-time: O(n^2), memory: O(1)
    public static int[] selectionSort(int[] nums){
        // keep track of sorting list
        int i = 0;
        // keep track of unsorting list
        int j = 0;
        // keep track of lowest number in a list
        int k = 0;

        // sort the whole array
        while(i < nums.length) {
            j = i;
            k = i;

            // find the lowest number in unsorted list
            while (j < nums.length) {
                if (nums[j] < nums[k]) {
                    k = j;
                }
                j++;
            }

            // swap the lowest number to the back of sorted array
            swap(i++, k, nums);
        }

        return nums;
    }

    /**
     * 1. compare every two elements, swap them if necessary
     * 2. repeat step 1 until finish compare the while array
     * 3. repeat step 1 and 2 until there is no swap (all element are sorted)
     * **/
    // run-time: O(n^2), memory: O(1)
    public static int[] bubbleSort(int[] nums){
        boolean isAllSorted = false;

        // sort until the array is completely sorted
        while (!isAllSorted) {
            isAllSorted = true;
            // sort pair by pair
            for (int i = 0; i < nums.length; i++) {
                if (i + 1 < nums.length && nums[i] > nums[i + 1]) {
                    isAllSorted = false;
                    swap(i, i + 1, nums);
                }
            }
        }

        return nums;
    }

    /**
     * 1. compare the back-most element in a sorted list with the front-most element (target) in an unsorted list and swap is necessary
     * 2. keep comparing the target to the elements in sorted list (back to front-most) until find the right position to insert
     * 3. keep repeat step 1 and 2 until an sorted array covers the whole array (nums.length times)
     * **/
    // run-time: O(n^2), memory: O(1)
    public static int[] insertionSort(int[] nums){
        // keep track of the end a sorted list
        int i = 0;
        // keep tract of elements in a sorted list
        int j = 0;
        // keep track of target elements in an unsorted list
        int k = 0;

        // repeat until the whole array is sorted
        while(i + 1 < nums.length && i < nums.length){
            j = i;
            k = i + 1;

            // insert the first element in an unsorted list to the right position in sorted list by:
            // swap the first unsorted target element with the sorted elements (back-most to front-most of a sorted list)
            // until a right position is found
            while(j >= 0 && nums[j] > nums[k]){
                swap(j--, k--, nums);
            }

            // grow a sorted list by 1 element
            i++;
        }

        return nums;
    }

    /***
     * 1. divide array into left and right partitions
     * 2. recursively call on left and right until entire array is sorted
     * ***/
    // runtime av: O(nlog(n)), memory: O(1)
    public static int[] quickSort(int[] nums, int start, int end){
        if (start <= end) {
            // divide
            int patitionIndex = partition(nums, start, end);

            // call quick sort on the left
            quickSort(nums, start, patitionIndex - 1);

            // call quick sort on the right
            quickSort(nums, patitionIndex + 1, end);
        }
        return nums;
    }

    /***
     * 1. select a pivot (front-most), declare start pointer, and end pointer
     * 2. move start pointer forward and compare the element with pivot
     * 3. if start pointer element is greater than pivot, stop start pointer:
     * 3.1 move end pointer until it find an element that is less than pivot.
     * 3.2 swap start pointer element with end pointer element
     * 4. Keep doing step 3 until start pointer passes end pointer
     * 4. if start pointer passes end pointer, swap end pointer element with pivot element
     * ***/
    // put elements into left and right: runtime: O(n), memory: O(1)
    private static int partition(int[] nums, int start, int end){
        // Note: if want to random index, we just pick a random middle element. Then swap it with the left-most element.
        // swap(nums, randomElementIndex, start);

        int pivotIndex = start;
        int pivot = nums[pivotIndex];

        // start pointer
        int i = pivotIndex + 1;

        // end pointer
        int j = end;

        // loop until start pointer passes end pointer
        while (i <= j){
            // stop when nums[i] is greater than pivot
            while(i < nums.length && nums[i] <= pivot){
                i++;
            }

            // stop when nums[j] is less than pivot
            while (j > 0 && nums[j] > pivot){
                j--;
            }

            // swap end pointer and start pointer element
            if(i <= j) {
                swap(i, j, nums);
            }
        }

        // swap pivot and end pointer element
        swap(pivotIndex, j, nums);

        return j;
    }
}
