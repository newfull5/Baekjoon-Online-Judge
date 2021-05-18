import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // TEST CASE
        int T = sc.nextInt();

        for (int t = 0; t < T; t++){
            String string = sc.next();

            String[] strarr = string.split("");
    
            int answer = 0;
            int cnt = 0;
    
            for (int i = 0; i < strarr.length; i++){
                
                if (strarr[i].equals("O")){
                    cnt += 1;
                    
                    answer += cnt;
                }
                else{
                    cnt = 0;
                }
            }
    
            System.out.println(answer);
        }
        
    }    
}
