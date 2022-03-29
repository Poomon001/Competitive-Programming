import java.util.Arrays;
public class MergeSort {
    public static void main(String[] args) {
        System.out.println("\n+=== merge sort in-place ===+\n");
        int[] nums1 = {5,1,1,2,0,8,9,0};
        int[] nums2 = {3,9,8,4};
        int[] nums3 = {};
        int[] nums4 = {64,25,12,22,11,-10, 78};
        int[] nums5 = {0,1,2,3,4,5,6,7};

        mergeSort_inPlace(nums1);
        for(int i:nums1){
            System.out.print(i + " ");
        }
        System.out.println("");

        mergeSort_inPlace(nums2);
        for(int i:nums2){
            System.out.print(i + " ");
        }
        System.out.println("");

        mergeSort_inPlace(nums3);
        for(int i:nums3){
            System.out.print(i + " ");
        }
        System.out.println("");

        mergeSort_inPlace(nums4);
        for(int i:nums4){
            System.out.print(i + " ");
        }
        System.out.println("");

        mergeSort_inPlace(nums5);
        for(int i:nums5){
            System.out.print(i + " ");
        }
        System.out.println("");

        System.out.println("\n+=== merge sort ===+\n");
        int[] nums6 = {5,1,1,2,0,8,9,0};
        int[] nums7 = {3,9,8,4};
        int[] nums8 = {};
        int[] nums9 = {64,25,12,22,11,-10, 78};
        int[] nums10 = {0,1,2,3,4,5,6,7};

        for(int i:mergeSort(nums6)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:mergeSort(nums7)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:mergeSort(nums8)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:mergeSort(nums9)){
            System.out.print(i + " ");
        }
        System.out.println("");

        for(int i:mergeSort(nums10)){
            System.out.print(i + " ");
        }
        System.out.println("");
    }

    /***
     * 1. divide array by half into left and right arrays
     * 2. recursively call on left and right until 1 element left in each array
     * 3. merge left and right already sorted arrays from step#2 (1 element array is a already sorted array)
     * 4. recursively merge left and right array until we get the whole list sorted
     * ***/
    public static void mergeSort_inPlace(int[] nums){
        // base case when array contains only 1 element
        if(nums.length <= 1){
            return;
        }

        // split
        int mid = nums.length/2;
        int[] left = Arrays.copyOfRange(nums, 0, mid);
        int[] right = Arrays.copyOfRange(nums, mid, nums.length);
        mergeSort_inPlace(left);
        mergeSort_inPlace(right);

        // merge
        mergeTwoSortedArray_inPlace(left, right, nums);
    }

    /***
     * a basic 3 pointers algo to merge two sorted arrays
     * ***/
    private static void mergeTwoSortedArray_inPlace(int[] arr1, int[] arr2, int[] nums){
        int i = 0; // keep track of arr1
        int j = 0; // keep track of arr2
        int k = 0; // keep track of merge array

        while(i < arr1.length && j < arr2.length){
            if(arr1[i] > arr2[j]){
                nums[k++] = arr2[j++];
            }else{
                nums[k++] = arr1[i++];
            }
        }

        while(i < arr1.length){
            nums[k++] = arr1[i++];
        }

        while(j < arr2.length){
            nums[k++] = arr2[j++];
        }
    }

    /***
     * 1. divide array by half into left and right arrays
     * 2. recursively call on left and right until 1 element left in each array
     * 3. merge left and right already sorted arrays from step#2 (1 element array is a already sorted array)
     * 4. recursively merge left and right array until we get the whole list sorted
     * ***/
    public static int[] mergeSort(int[] nums){
        // base case when array contains only 1 element
        if(nums.length <= 1){
            return nums;
        }

        int mid = nums.length/2;
        int[] left = Arrays.copyOfRange(nums, 0, mid);
        int[] right = Arrays.copyOfRange(nums, mid, nums.length);

        left = mergeSort(left);
        right = mergeSort(right);

        return mergeTwoSortedArray(left, right);
    }

    /***
     * a basic 3 pointers algo to merge two sorted arrays
     * ***/
    private static int[] mergeTwoSortedArray(int[] arr1, int[] arr2){
        int[] mergeArray = new int[arr1.length + arr2.length];
        int i = 0; // keep track of arr1
        int j = 0; // keep track of arr2
        int k = 0; // keep track of merge array

        while(i < arr1.length && j < arr2.length){
            if(arr1[i] > arr2[j]){
                mergeArray[k++] = arr2[j++];
            }else{
                mergeArray[k++] = arr1[i++];
            }
        }

        while(i < arr1.length){
            mergeArray[k++] = arr1[i++];
        }

        while(j < arr2.length){
            mergeArray[k++] = arr2[j++];
        }

        return  mergeArray;
    }
}
