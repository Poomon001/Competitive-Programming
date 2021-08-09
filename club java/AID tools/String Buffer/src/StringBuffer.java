import java.util.Arrays;
import java.util.Scanner;

public class StringBuffer {
    public static void main(String[] args) {
        String x = "pqwpoom";
        java.lang.StringBuffer y = new java.lang.StringBuffer(x);
        String z = y.reverse().toString();
        y.insert(0, "my name is ");
        y.replace(0, 1, "z");
        int i = 0;
        char[] c = x.toCharArray();
        x.toUpperCase();
        System.out.println(x);
        int a[] = {5, 1, 2, 3};
        Arrays.sort(c);
        for (char o : c) {
            System.out.println(o);
        }
        try {
            int u = 2 / 0;
        } catch (ArithmeticException e) {
            System.out.println(e);
            throw new ArithmeticException(e.toString());
        }
    }
}
