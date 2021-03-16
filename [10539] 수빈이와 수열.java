import java.util.Scanner;

public class Main{

    public static int sum(int[] arr){
        int outputs = 0;
        for (int i = 0; i < arr.length; i++){
            outputs += arr[i];
        }
        return outputs;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int arr_length = sc.nextInt();
        int arr[] = new int[arr_length];
        int answer[] = new int[arr_length];

        for (int i = 0; i < arr_length; i++){
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < arr_length; i++){
            answer[i] = arr[i] * (i+1) - sum(answer);
        }

        for (int i = 0; i < arr_length; i++){
            System.out.print(answer[i]);
            System.out.print(" ");
        }
    }
}
