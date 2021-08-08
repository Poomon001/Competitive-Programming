import java.util.Scanner;

class anotherCandies {

	/*
	 * Purpose: Find out whether the teacher can divide the candies into N exactly equal heaps.
	 * Parameters: none
	 * Returns: none
	 * Post-Condition: none
	 */
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);

		int numCase = kb.nextInt();

		for(int i = 0; i < numCase; i++){
			System.out.println("");
			int numChildren = kb.nextInt();
			long sumCandies = 0;

			// find sumCandies from all student (modulo to reduce the size of number)
			for (int j = 0; j < numChildren; j++) {
				long numCandies = kb.nextLong();
				sumCandies = (sumCandies + numCandies) % numChildren;
			}//for

			// print YES if all students get the same number of candies (sumCandies/numChildren gives 0 reminder)
			System.out.println(sumCandies % numChildren == 0 ? "YES" : "NO");
		}//while
	}
}

