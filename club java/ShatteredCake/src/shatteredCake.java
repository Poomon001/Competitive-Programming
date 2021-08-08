import java.util.Scanner;
public class shatteredCake {

	/*
	 * Link: https://open.kattis.com/problems/shatteredcake
	 * Purpose: Find out the length L of the cake.
	 * input: on the first line, the width W of the cake
		    : on the second line, the number N of shattered pieces
			: on each of the next N lines, the width wi and length li of each piece
	 * Returns: none
	 * Post-Condition: none
	 */
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		int W = 0;
		int area = 0;
		int piece = 0;
		int smallArea2 = 0;
		String widthLength = "";

		W = kb.nextInt();
		piece = kb.nextInt();
		kb.nextLine();

		// handdle input and find area
		for(int i =0;i < piece; i++) {
			widthLength  = kb.nextLine();
			String [] smallArea = widthLength.split(" ");
			smallArea2 = Integer.parseInt(smallArea[1]) * Integer.parseInt(smallArea[0]);

			area = area + smallArea2;
		}//for

		// find length
		System.out.print(area/W);

	}
}
