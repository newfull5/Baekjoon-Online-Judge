import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true){

            int N = sc.nextInt();
            if (N == 0){ break; }
            int P = sc.nextInt();
            boolean breakpoint = false;

            for (int i=0; i<N/4; i++){
                int[] arr = {2*i+1, 2*i+2, N-2*i-1, N-2*i};

                for (int j=0; j<4; j++){
                    if (arr[j] == P){
                        breakpoint = true;
                        break;
                    }
                }

                if (breakpoint == true){
                    for (int j=0; j<4; j++){
                        if (arr[j] != P){
                            System.out.println(arr[j]);
                        }
                    }
                    break;
                }
            }
        }       
    }    
}
