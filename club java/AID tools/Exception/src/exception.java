/** try...catch will not stop file from running but throw will stop **/
public class exception {
    public static void main(String[] args){
        runTimeException();
        requirementException(-1);
    }
    public static void runTimeException(){
        try{
            // int z = 1/0;
            int [] x = new int[1];
            x[2] = 0;
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println("a");
            System.out.println(e);

            // if want the program to terminate after catch
            // throw new ArrayIndexOutOfBoundsException();
        }catch(ArithmeticException e){
            System.out.println("b");
            System.out.println(e);

            // if want the program to terminate after catch
            // throw new ArithmeticException();
          }catch(Exception e){
            System.out.println("c");
            System.out.println(e);

            // if want the program to terminate after catch
            // throw new RuntimeException(e.toString());
        }
    } // runtimeException

    // requirement: input will never be negative
    public static void requirementException(int x){
        if (x > 0){
            System.out.println("valid");
        }else{
            // throw new IllegalArgumentException();
            throw new IllegalArgumentException("Argument cannot be negative"); // specify the error
        }
    }
}
