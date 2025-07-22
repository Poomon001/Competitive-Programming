import java.util.ArrayList;
import java.util.concurrent.ConcurrentHashMap;

/*
    * Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
    * Purpose: Implement the RandomizedSet class
    * Parameters: None
    * Returns: None
    * Pre-Condition: -2^31 <= val <= 2^31 - 1
                   : At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
                   : There will be at least one element in the data structure when getRandom is called.
      Post-Condition : Must complete within O(1) runtime
*/
public class InsertDeleteGetRandom {
    private ArrayList<Integer> values;
    private ConcurrentHashMap<Integer, Integer> valueToIndex;

    // RandomizedSet() Initializes the RandomizedSet object.
    public InsertDeleteGetRandom() {
        // {value, index}
        valueToIndex = new ConcurrentHashMap<>();
        values = new ArrayList<>();
    }

    // bool insert(int val) Inserts an item val into the set if not present.
    // Returns true if the item was not present, false otherwise.
    public boolean insert(int val) {
        if(this.valueToIndex.containsKey(val)) {
            return false;
        }
        this.values.add(val);
        this.valueToIndex.put(val, values.size() - 1);
        return true;
    }

    // bool remove(int val) Removes an item val from the set if present.
    // Returns true if the item was present, false otherwise.
    public boolean remove(int val) {
        if(!this.valueToIndex.containsKey(val)) {
            return false;
        }

        // remove val from HashMap
        int index = this.valueToIndex.remove(val);

        // O(1) remove val from arraylist
        int lastIndex = this.values.size() - 1;
        int lastElement = this.values.get(lastIndex);
        this.values.set(index, lastElement);
        this.values.remove(lastIndex);

        // update swapped index in HashSet
        this.valueToIndex.replace(lastElement, index); // update only if key exist, save for last element removed

        return true;
    }

    // int getRandom() Returns a random element from the current set of elements
    // (it's guaranteed that at least one element exists when this method is called).
    // Each element must have the same probability of being returned.
    public int getRandom() {
        int size = this.valueToIndex.size();
        int rand = (int)(Math.random() * size);
        return this.values.get(rand);
    }

    public static void main(String[] args) {
        System.out.println("\n === test 1 === \n");
        InsertDeleteGetRandom randomizedSet1 = new InsertDeleteGetRandom();
        System.out.println(randomizedSet1.insert(1)); // true
        System.out.println(randomizedSet1.remove(2)); // false
        System.out.println(randomizedSet1.insert(2)); // true
        System.out.println(randomizedSet1.getRandom()); // [1 or 2]
        System.out.println(randomizedSet1.remove(1)); // true
        System.out.println(randomizedSet1.insert(2)); // false
        System.out.println(randomizedSet1.getRandom()); // [2]

        System.out.println("\n === test 2 === \n");
        InsertDeleteGetRandom randomizedSet2 = new InsertDeleteGetRandom();
        System.out.println(randomizedSet2.remove(0)); // false
        System.out.println(randomizedSet2.remove(0)); // false
        System.out.println(randomizedSet2.insert(0)); // true
        System.out.println(randomizedSet2.getRandom()); // [0]
        System.out.println(randomizedSet2.remove(0)); // true
        System.out.println(randomizedSet2.insert(0)); // true

        System.out.println("\n === test 3 === \n");
        InsertDeleteGetRandom randomizedSet3 = new InsertDeleteGetRandom();
        System.out.println(randomizedSet3.insert(-1)); // true
        System.out.println(randomizedSet3.remove(-2)); // false
        System.out.println(randomizedSet3.insert(-2)); // true
        System.out.println(randomizedSet3.getRandom()); // [-1 or -2]
        System.out.println(randomizedSet3.remove(-1)); // true
        System.out.println(randomizedSet3.insert(-2)); // false
        System.out.println(randomizedSet3.getRandom()); // [-2]
    }
}
