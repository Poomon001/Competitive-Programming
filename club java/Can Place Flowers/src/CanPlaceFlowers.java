public class CanPlaceFlowers {
    public static void main(String[] args) {
        int[] flowerbed1 = {1,0,0,0,1};
        int[] flowerbed2 = {1};
        int[] flowerbed3 = {0};
        int[] flowerbed4 = {1,0};
        int[] flowerbed5 = {0,0};
        int[] flowerbed6 = {0,1};
        int[] flowerbed7 = {1,0,1};
        int[] flowerbed8 = {1,0,0};
        int[] flowerbed9 = {1,0,1};
        int[] flowerbed10 = {1,0,0,1,0};

        System.out.println(canPlaceFlowers(flowerbed1, 1)); // true
        System.out.println(canPlaceFlowers(flowerbed1, 2)); // false
        System.out.println(canPlaceFlowers(flowerbed2, 1)); // false
        System.out.println(canPlaceFlowers(flowerbed3, 1)); // true
        System.out.println(canPlaceFlowers(flowerbed4, 1)); // false
        System.out.println(canPlaceFlowers(flowerbed5, 1)); // true
        System.out.println(canPlaceFlowers(flowerbed6, 1)); // false
        System.out.println(canPlaceFlowers(flowerbed7, 1)); // false
        System.out.println(canPlaceFlowers(flowerbed8, 1)); // true
        System.out.println(canPlaceFlowers(flowerbed9, 1)); // false
        System.out.println(canPlaceFlowers(flowerbed10, 1)); // false
    }

    // runtime: O(n), memory: O(1)
    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        int i = 0;
        int prevPot = 0;
        int nextPot = 0;

        // n is already 0 then it is valid
        if(n == 0){
            return true;
        }

        // place flower if possbile
        while(i < flowerbed.length && n != 0){
            // get next pot
            if(i+1 < flowerbed.length){
                nextPot = flowerbed[i+1];
            }

            // skip if the curr pot is full, prev Pot is full, or next pot is full. Oterwise place a flower.
            if(flowerbed[i] == 1 || prevPot == 1 || nextPot == 1){
                prevPot = flowerbed[i];
            }else{
                // place a flower
                prevPot = 1;
                n--;
            }
            i++;
        }
        return n <= 0? true:false;
    }
}
