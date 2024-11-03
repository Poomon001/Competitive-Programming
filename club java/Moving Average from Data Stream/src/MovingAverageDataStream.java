public class MovingAverageDataStream {
    public static void main(String[] args) {
        System.out.println("\n total objects:" + MovingAverage.sumObj + "\n total nexts:" + MovingAverage.sumNext);

        MovingAverage obj1 = new MovingAverage(3);
        System.out.println(obj1.next(2)); // 2
        System.out.println(obj1.next(5)); // 3.5
        System.out.println(obj1.next(5)); // 4
        System.out.println(obj1.next(5)); // 5
        System.out.println(obj1.next(3)); // 4.333
        System.out.println(obj1.next(12)); // 6.667
        System.out.println(obj1.next(3)); // 6

        System.out.println("\n total objects:" + MovingAverage.sumObj + "\n total nexts:" + MovingAverage.sumNext);

        MovingAverage obj2 = new MovingAverage(1);
        System.out.println(obj2.next(2)); // 2
        System.out.println(obj2.next(5)); // 5
        System.out.println(obj2.next(5)); // 5
        System.out.println(obj2.next(5)); // 5
        System.out.println(obj2.next(3)); // 3
        System.out.println(obj2.next(12)); // 12
        System.out.println(obj2.next(3)); // 3

        System.out.println("\n total objects:" + MovingAverage.sumObj + "\n total nexts:" + MovingAverage.sumNext);

        MovingAverage obj3 = new MovingAverage(10);
        System.out.println(obj3.next(2)); // 2
        System.out.println(obj3.next(5)); // 3.5
        System.out.println(obj3.next(5)); // 4
        System.out.println(obj3.next(5)); // 4.25
        System.out.println(obj3.next(3)); // 4
        System.out.println(obj3.next(12)); // 5.333
        System.out.println(obj3.next(3)); // 5

        System.out.println("\n total objects:" + MovingAverage.sumObj + "\n total nexts:" + MovingAverage.sumNext);
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
    public static class MovingAverage {
        public static int sumObj = 0;
        public static int sumNext = 0;
        int[] window;
        double total = 0;
        int pointer = 0;
        int currSize = 0;

        // Initializes the object with the size of the window size
        public MovingAverage(int size) {
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
}

