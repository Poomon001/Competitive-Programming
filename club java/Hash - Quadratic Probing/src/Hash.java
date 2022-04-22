import java.util.*;

public class Hash{
    public static void main(String[] args) {
        MyHash hash1 = new MyHash();
        hash1.add("uk");
        hash1.add("canada");
        hash1.add("china");
        hash1.add("usa");
        hash1.add("usa");
        hash1.add("usa");

        System.out.println(hash1.find("usa")); // 116099
        System.out.println(hash1.contains("usa")); // true
        System.out.println(hash1.contains("canada")); // true
        System.out.println(hash1.contains("india")); // false
        System.out.println(hash1.get(1)); // null
        System.out.println(hash1.get(116099)); // usa
        System.out.println(hash1.get(116100)); // usa (116099 + 2^1)
        System.out.println(hash1.get(116101)); // null
        System.out.println(hash1.get(116103)); // usa (116099 + 2^2)
    }
}

class MyHash {
    public static final int TableSize = 226226;
    List<String> hashSet;

    MyHash(){
        int N = this.TableSize;

        hashSet = new ArrayList<>();

        // init hash table space
        for(int i = 0; i < N; i++){
            this.hashSet.add(null);
        }
    }

    // hash function: convert value to index
    private int hash(String s){
        int N = this.TableSize;
        int m = s.length();
        int p = 31;

        // get ascii value
        long ascii = 0;
        for(int i = 0; i < s.length(); i++){
            ascii += (long)Integer.valueOf(s.charAt(i))*Math.pow(p, m-i-1);
        }

        // find hash value
        long hashValue = (ascii)%N;

        return (int)hashValue;
    }

    /* insert(s)
       Insert the value s into the hash table and return the index at
       which it was stored.
    */
    public int add(String s) {
        //Get the hash value of the string and start the search at that index.
        int i = hash(s);
        int m = this.TableSize;

        /*** quadratic probing ***/
        int loopCounter = 1;
        int index = i ;
        while(this.hashSet.get(index) != null && !this.hashSet.get(index).equals("-1")){
            int pow = (int)Math.pow(loopCounter++, 2);
            index = i + pow;

            // reach the end of the array. reset i
            if(index >= m){
                index = index%m;
            }
        }
        i = index;
        this.hashSet.set(i, s);
        return i;
    }

    /* find(s)
       Search for the string s in the hash table. If s is found, return
       the index at which it was found. If s is not found, return -1.
    */
    public int find(String s){
        //Get the hash value of the string and start the search at that index.
        int i = hash(s);
        int m = this.TableSize;

        /*** quadratic probing ***/
        int loopCounter = 1;
        int index = i;
        while(this.hashSet.get(index) != null && !this.hashSet.get(index).equals(s)){
            int pow = (int)Math.pow(loopCounter++, 2);
            index = i + pow;

            // reach the end of the array. reset i
            if(index >= m){
                index = index%m;
            }
        }
        i = index;
        // if get into null, then target doesn't exist
        if(this.hashSet.get(i) == null){
            return -1;
        }

        return i;
    }

    public boolean contains(String s){
        if(this.find(s) != -1){
            return true;
        }
        return false;
    }

    public String get(int i){
        return this.hashSet.get(i);
    }
}
