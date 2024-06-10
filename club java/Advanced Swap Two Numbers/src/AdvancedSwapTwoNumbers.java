public class AdvancedSwapTwoNumbers {
    public AdvancedSwapTwoNumbers() {
    }

    public static void main(String[] args){
        Pair pair1 = new Pair(1, 2);
        System.out.println("\n === test 1 ===\n");
        System.out.println(pair1);
        System.out.println(swap_m1(pair1));
        System.out.println(swap_m2(pair1));
        System.out.println(swap_m3(pair1));

        Pair pair2 = new Pair(6, 0);
        System.out.println("\n === test 2 ===\n");
        System.out.println(pair2);
        System.out.println(swap_m1(pair2));
        System.out.println(swap_m2(pair2));
        System.out.println(swap_m3(pair2));

        Pair pair3 = new Pair(1, -2);
        System.out.println("\n === test 3 ===\n");
        System.out.println(pair3);
        System.out.println(swap_m1(pair3));
        System.out.println(swap_m2(pair3));
        System.out.println(swap_m3(pair3));

        Pair pair4 = new Pair(-1, -2);
        System.out.println("\n === test 4 ===\n");
        System.out.println(pair4);
        System.out.println(swap_m1(pair4));
        System.out.println(swap_m2(pair4));
        System.out.println(swap_m3(pair4));

        Pair pair5 = new Pair(-2, -1);
        System.out.println("\n === test 5 ===\n");
        System.out.println(pair5);
        System.out.println(swap_m1(pair5));
        System.out.println(swap_m2(pair5));
        System.out.println(swap_m3(pair5));
    }

    // temp swap - runtime: O(1), memory: O(1) with a temporary storage
    public static Pair swap_m1(Pair pair){
        int temp = 0;
        int x = pair.getX();
        int y = pair.getY();

        temp = x;
        x = y;
        y = temp;
        return new Pair(x, y);
    }

    // Math - runtime: O(1), memory: O(1) without a temporary storage
    public static Pair swap_m2(Pair pair){
        int x = pair.getX();
        int y = pair.getY();

        // x = z = y - x
        // y = y - z = y - (y - x) = x
        // x = z + x = y - x + x = y
        x = y - x;
        y = y - x;
        x = x + y;
        return new Pair(x, y);
    }

    // XOR - runtime: O(1). memory: O(1) without a temporary storage
    public static Pair swap_m3(Pair pair){
        int x = pair.getX();
        int y = pair.getY();

        // a XOR a = 0
        // a XOR 0 = a
        // a XOR b XOR a XOR 0 = (a XOR a) XOR (b XOR 0) = b
        x = x ^ y; // z = x ^ y
        y = y ^ x; // y ^ (x ^ y) = x
        x = y ^ x; // x ^ (x ^ y) = y
        return new Pair(x, y);
    }
}

final class Pair {
    private int x;
    private int y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String toString(){
        return String.format("x: [%d], y: [%d]", this.x, this.y);
    }
}
