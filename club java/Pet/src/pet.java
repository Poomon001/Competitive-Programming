import java.util.Scanner;
public class pet {

	/*
     * Link: https://open.kattis.com/problems/pet
     * Purpose: Write a program that determines the winner and how many points they got.
     * Parameters: none
     * Returns: none
     * Post-Condition: none
     */
    public static void main(String[] args) {

			Scanner scan = new Scanner(System.in);
			int sum1 = 0;
			int result = 0;
			int winner = 0;

			int a[][] = new int[5][4];

			 // get 4 integers per line
			 for(int i=0; i<4;i++){
		            for(int j=0; j<4;j++){
		                a[i][j]=scan.nextInt();
		            }//for
		         }//for

		     // total of 5 line and find sum of 4 integer of each line
			 for(int i=0; i<5;i++){ 
			 	sum1 = 0;
	            for(int j=0; j<4;j++){
	              sum1 = sum1 + a[i][j];
	            }//for

			    // find the line with highest sum
	            if (sum1 > result) {
	            	result = sum1;
	            	winner = i;
	            }
	         }//for
			 System.out.println(winner+1 + " " + result);
	
	}
}