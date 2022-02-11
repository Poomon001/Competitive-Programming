//Template is created by Zhuoli Xiao, on Sept. 19st, 2016.
//Only used for Lab 226, 2016 Fall.
//All Rights Reserved.

//modified by Rich Little on Sept. 23, 2016
//modified by Rich Little on May 12, 2017
//modified by Poomrapee Chuthamsatid on Jan 28, 2022


import java.util.Random;
public class QuickSelect {
    //Function to invoke quickSelect
    public static int QS(int[] S, int k){
        // catch an array with one element
        if (S.length==1)
            return S[0];

        return quickSelect(0,S.length-1,S,k);

    }

    //do quickSelect in a recursive way
    private static int quickSelect(int left,int right, int[] array, int k){
        int kIndex = k-1;

        //TODO pick a random pivot
        int pivotIndex = pickRandomPivot(left, right);

        //TODO do the partition based on the pivot
        int pIndex = partition(left, right, array, pivotIndex);

        //TODO recursive call for quickSelect
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

    //TODO do Partition with a pivot
    private static int partition(int left, int right, int[] array, int pIndex){
        // swap random pIndex and left-most element
        swap(array, pIndex, left);

        int pivotIndex = left;
        int pivot = array[pivotIndex];
        left = pivotIndex + 1;

        // stop when left index cross right index
        while(left <= right){
            while(left < array.length && pivot >= array[left]){
                left++;
            }

            while(right > 0 && pivot < array[right]){
                right--;
            }

            // stop when left index cross right index
            if (left <= right) {
                swap(array, right, left);
            }
        }

        swap(array, pivotIndex, right);

        // Kth index of pivot
        return right;

    }

    //Pick a random pivot to do the QuickSelect
    private static int pickRandomPivot(int left, int right){
        int index=0;
        Random rand= new Random();
        index = left+rand.nextInt(right-left+1);
        return index;
    }

    //swap two elements in the array
    private static void swap(int[]array, int a, int b){
        int tmp = array[a];
        array[a] = array[b];
        array[b] = tmp;
    }

    /***
     * Find an Kth smallest element in an array
     * ***/
    //Our main function to test the algorithm
    public static void main (String[] args){
        //array one has duplicate elements
        int[] array1 ={12,13,17,14,21,3,4,9,21,8};
        //sorted array1 = {3,4,8,9,12,13,14,17,21,21}

        int[] array2 ={14,8,22,18,6,2,15,84,13,12};
        //sorted array2 = {2,6,8,12,13,14,15,18,22,84}

        int[] array3 ={6,8,14,18,22,2,12,13,15,84};

        int[] array4 = {1,2};

        int[] array5 = {1,1,1,2,2,4};

        System.out.println("Correct answer is 12 = " + "Your answer: "+QS(array1,5));
        System.out.println("Correct answer is 21 = " + "Your answer: "+QS(array1,10));

        System.out.println("Correct answer is 15 = " + "Your answer: "+QS(array2,7));
        System.out.println("Correct answer is 13 = " + "Your answer: "+QS(array3,5));
        System.out.println("Correct answer is 1 = " + "Your answer: "+QS(array4,1));
        System.out.println("Correct answer is 2 = " + "Your answer: "+QS(array5,5));
    }
}

