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

    public static class MovingAverage {
        public static int sumObj = 0;
        public static int sumNext = 0;
        int[] window;
        double total = 0;
        int pointer = 0;
        int currSize = 0;

        public MovingAverage(int size) {
            this.window = new int[size];
            this.sumObj++;
        }

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

