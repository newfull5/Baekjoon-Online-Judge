import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String string = sc.nextLine();

        string = string.replace("c=", "č");
        string = string.replace("c-", "ć");
        string = string.replace("dz=", "A");
        string = string.replace("d-", "đ");
        string = string.replace("lj", "A");
        string = string.replace("nj", "A");
        string = string.replace("s=", "š");
        string = string.replace("z=", "ž");

        System.out.println(string.length());
    }
}
