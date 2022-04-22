import java.util.*;

public class Hash {
    public static void main(String[] args) {
        MyHashSet hash1 = new MyHashSet();
        hash1.add(10);
        hash1.add(1);
        hash1.add(4);
        hash1.add(5);
        System.out.println(hash1.contains(9)); // false
        System.out.println(hash1.contains(10)); // true
        hash1.add(6);
        hash1.remove(10);
        System.out.println(hash1.contains(10)); // false
        System.out.println(hash1.contains(6)); // true
    }
}

/**
 * Link: https://leetcode.com/problems/design-hashset/
 * Purpose: Design a HashSet without using any built-in hash table libraries.
 * Parameters: None
 * Returns: None
 * Pre-Condition: 0 <= key <= 106
 * Post-Condition : None
 **/
class MyHashSet {
    final static int SIZE = 100;
    List<List<Integer>> hashSet;

    // chaining appraoch
    public MyHashSet() {
        this.hashSet = new ArrayList();
        for(int i = 0; i < this.SIZE; i++){
            this.hashSet.add(null);
        }
    }

    // runtime: O(1) ; a = length of the chain
    public void add(int key) {
        // hash function
        int index = key%this.SIZE;

        // get a chain at the index
        List<Integer> inner = this.hashSet.get(index);

        // if there is no chain, init the chain
        if(inner == null){
            List<Integer> list = new ArrayList();
            list.add(key);
            this.hashSet.set(index, list);
        }else

            // if no dulpicate value, add it in
            if(!inner.contains(key)){
                inner.add(key);
                this.hashSet.set(index, inner);
            }
    }

    // runtime: O(a) ; a = length of the chain
    public void remove(int key) {
        // hash function
        int index = key%this.SIZE;

        // get a chain at the index
        List<Integer> inner = this.hashSet.get(index);

        if(inner !=null){
            for(int i = 0; i < inner.size();i++){
                if(inner.get(i) == key){
                    inner.remove(i);
                    this.hashSet.set(index, inner);
                }
            }
        }
    }

    // runtime: O(a) ; a = length of the chain
    public boolean contains(int key) {
        // hash function
        int index = key%this.SIZE;

        // get a chain at the index
        List<Integer> inner = this.hashSet.get(index);
        if(inner == null){
            return false;
        }

        for(int i = 0; i < inner.size();i++){
            if(inner.get(i) == key){
                return true;
            }
        }
        return false;
    }
}

