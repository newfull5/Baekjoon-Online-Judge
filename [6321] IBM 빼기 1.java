import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 1; t<=T; t++){

            String s = sc.next();
            System.out.println("String #"+t);

            for (int i = 0; i<s.length(); i++){
                if (s.charAt(i) == 'Z'){
                    System.out.print("A");
                }
                else{
                    System.out.print((char) ((int) s.charAt(i) + 1));    
                }
            }
            System.out.println();
            System.out.println();
        }
    }    
}
