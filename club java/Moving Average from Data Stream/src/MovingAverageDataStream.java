import java.util.LinkedList;
import java.util.Queue;

public class MovingAverageDataStream {
    public static void main(String[] args) {
        System.out.println("\n === Solution 1 === \n");
        System.out.println("\n total objects:" + MovingAverage_M1.sumObj + "\n total nexts:" + MovingAverage_M1.sumNext);

        MovingAverage_M1 obj1 = new MovingAverage_M1(3);
        System.out.println(obj1.next(2)); // 2
        System.out.println(obj1.next(5)); // 3.5
        System.out.println(obj1.next(5)); // 4
        System.out.println(obj1.next(5)); // 5
        System.out.println(obj1.next(3)); // 4.333
        System.out.println(obj1.next(12)); // 6.667
        System.out.println(obj1.next(3)); // 6

        System.out.println("\n total objects:" + MovingAverage_M1.sumObj + "\n total nexts:" + MovingAverage_M1.sumNext);

        MovingAverage_M1 obj2 = new MovingAverage_M1(1);
        System.out.println(obj2.next(2)); // 2
        System.out.println(obj2.next(5)); // 5
        System.out.println(obj2.next(5)); // 5
        System.out.println(obj2.next(5)); // 5
        System.out.println(obj2.next(3)); // 3
        System.out.println(obj2.next(12)); // 12
        System.out.println(obj2.next(3)); // 3

        System.out.println("\n total objects:" + MovingAverage_M1.sumObj + "\n total nexts:" + MovingAverage_M1.sumNext);

        MovingAverage_M1 obj3 = new MovingAverage_M1(10);
        System.out.println(obj3.next(2)); // 2
        System.out.println(obj3.next(5)); // 3.5
        System.out.println(obj3.next(5)); // 4
        System.out.println(obj3.next(5)); // 4.25
        System.out.println(obj3.next(3)); // 4
        System.out.println(obj3.next(12)); // 5.333
        System.out.println(obj3.next(3)); // 5

        System.out.println("\n total objects:" + MovingAverage_M1.sumObj + "\n total nexts:" + MovingAverage_M1.sumNext);

        System.out.println("\n === Solution 2 === \n");

        System.out.println("\n total objects:" + MovingAverage_M2.sumObj + "\n total nexts:" + MovingAverage_M2.sumNext);

        MovingAverage_M2 obj4 = new MovingAverage_M2(3);
        System.out.println(obj4.next(2)); // 2
        System.out.println(obj4.next(5)); // 3.5
        System.out.println(obj4.next(5)); // 4
        System.out.println(obj4.next(5)); // 5
        System.out.println(obj4.next(3)); // 4.333
        System.out.println(obj4.next(12)); // 6.667
        System.out.println(obj4.next(3)); // 6

        System.out.println("\n total objects:" + MovingAverage_M2.sumObj + "\n total nexts:" + MovingAverage_M2.sumNext);

        MovingAverage_M2 obj5 = new MovingAverage_M2(1);
        System.out.println(obj5.next(2)); // 2
        System.out.println(obj5.next(5)); // 5
        System.out.println(obj5.next(5)); // 5
        System.out.println(obj5.next(5)); // 5
        System.out.println(obj5.next(3)); // 3
        System.out.println(obj5.next(12)); // 12
        System.out.println(obj5.next(3)); // 3

        System.out.println("\n total objects:" + MovingAverage_M2.sumObj + "\n total nexts:" + MovingAverage_M2.sumNext);

        MovingAverage_M2 obj6 = new MovingAverage_M2(10);
        System.out.println(obj6.next(2)); // 2
        System.out.println(obj6.next(5)); // 3.5
        System.out.println(obj6.next(5)); // 4
        System.out.println(obj6.next(5)); // 4.25
        System.out.println(obj6.next(3)); // 4
        System.out.println(obj6.next(12)); // 5.333
        System.out.println(obj6.next(3)); // 5

        System.out.println("\n total objects:" + MovingAverage_M2.sumObj + "\n total nexts:" + MovingAverage_M2.sumNext);
    }

    /**
     Link: https://leetcode.com/problems/moving-average-from-data-stream/
     Purpose: Calculate the moving average of all integers in the sliding window
     parameter: None
     return: None
     Pre-Condition: 1 <= size <= 1000
                  : -10^5 <= val <= 10^5
                  : At most 10^4 calls will be made to next.
     Post-Condition: none
     **/
    public static class MovingAverage_M1 {
        public static int sumObj = 0;
        public static int sumNext = 0;
        int[] window;
        double total = 0;
        int pointer = 0;
        int currSize = 0;

        // Initializes the object with the size of the window size
        public MovingAverage_M1(int size) {
            this.window = new int[size];
            this.sumObj++;
        }

        // Returns the moving average of the last size values of the stream
        public double next(int val) {
            this.sumNext++;
            // increase size
            if(this.currSize < window.length) {
                this.currSize++;
            }

            // update average
            this.total -= this.window[this.pointer];
            this.total += val;

            // add element to window
            this.window[this.pointer] = val;
            this.pointer = (this.pointer + 1) % window.length;

            return this.total / currSize;
        }
    }

    public static class MovingAverage_M2 {
        public static int sumObj = 0;
        public static int sumNext = 0;
        private int size;
        private Queue<Integer> nums;
        private double sum;

        public MovingAverage_M2(int size) {
            this.size = size;
            this.nums = new LinkedList<>();
            this.sum = 0;
            this.sumObj++;
        }

        public double next(int val) {
            this.sumNext++;
            if (nums.size() == size) {
                sum -= nums.poll();
            }

            nums.add(val);
            sum += val;
            return sum / nums.size();
        }
    }

}

