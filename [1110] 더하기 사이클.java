import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int start = sc.nextInt();

        int n = start;
        int cnt = 0;
        int a, b;
        while (true){
            cnt += 1;

            if (n < 10){
                a = 0;
                b = n;
            }
            else {
                b = n % 10;
                a = (n - b) / 10;
            }

            n = (b*10) + ((a+b) % 10);
            if (n==start){
                System.out.println(cnt);
                break;
            }
        }
    }
}
