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

//        System.out.println("\n+=== merge sort ===+\n");
//        int[] nums6 = {5,1,1,2,0,8,9,0};
//        int[] nums7 = {3,9,8,4};
//        int[] nums8 = {};
//        int[] nums9 = {64,25,12,22,11,-10, 78};
//        int[] nums10 = {0,1,2,3,4,5,6,7};
//
//        for(int i:mergeSort(nums6)){
//            System.out.print(i + " ");
//        }
//        System.out.println("");
//
//        for(int i:mergeSort(nums7)){
//            System.out.print(i + " ");
//        }
//        System.out.println("");
//
//        for(int i:mergeSort(nums7)){
//            System.out.print(i + " ");
//        }
//        System.out.println("");
//
//        for(int i:mergeSort(nums8)){
//            System.out.print(i + " ");
//        }
//        System.out.println("");
//
//        for(int i:mergeSort(nums9)){
//            System.out.print(i + " ");
//        }
//        System.out.println("");
    }
    public static void mergeSort_inPlace(int[] nums){

    }
}
