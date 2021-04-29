import java.util.Scanner;

public class Main {
    
    static int Solution(int n){
        if (n < 100){
            return n;
        }

        if (n == 1000){
            return 144;
        }

        int answer = 0;

        for (int i=100; i<=n; i++){
            int a = i % 10;
            int b = (i/10) % 10;
            int c = (i/100) % 10;

            if (a-b == b-c){
                answer += 1;
            }
        }

        return answer + 99;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(Solution(sc.nextInt()));
    }
}
