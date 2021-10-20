import java.util.Scanner;

public class MissingNumbers {

    /*
     * Link: https://open.kattis.com/problems/missingnumbers
     * Purpose: If the child recited all the numbers between 1 and the last number they recited, then print good job.
              : If the child missed any numbers between 1 and the last number they recited,
     *          then print those missing numbers in increasing numeric order, one per line.
     * Parameters: none
     * Returns: none
     * Post-Condition: none
     */
    public static void main(String[] args) {
        int numList = 0;
        int count = 0;
        int mark = 0;
        int isGood = 0;
        Scanner kb = new Scanner(System.in);
        numList = kb.nextInt();
        for(int i = 0;i < numList; i++) {
            count = kb.nextInt();//numbeer that is counted

            for(int j = 1 + mark; j <= count; j++) {
                if(count != j) {
                    System.out.println(j);
                    isGood = 1;
                }
                mark = count ;
            }//if
        }
        if(isGood == 0) {
            System.out.println("good job");
        }
    }
}
