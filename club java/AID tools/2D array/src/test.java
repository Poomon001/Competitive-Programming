import java.util.Scanner;  // Import the Scanner cl
public class test {
    public static void main(String[] args){
        Scanner myObj = new Scanner(System.in);
        double x  = 3.99;
        int y = (int) x;
        mystery(2,1);
    }

    public static void mystery(int a ,int b) {
       int[][] x = {{1,2,3,4,5,6,7,8,9, 10},{0,1}};
       int[] y = new int[10];
       for (int i = 0; i < y.length;i++){
           y[i] = i;
       }
       for(int i =0;i< y.length;i++){
           System.out.println(y[i] == x[0][i]);
       }
    }
}
