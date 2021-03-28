import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int max = 0;
        int answer = 0;
        for (int n = 0; n < 9; n++){
            int temp = sc.nextInt();
            if (max < temp){
                max = temp;
                answer = n;
            }
        }
        System.out.println(max);
        System.out.println(answer+1);
    }
}
