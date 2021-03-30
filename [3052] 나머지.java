import java.util.HashSet;
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> set = new HashSet<>();

        for (int i=0; i<10; i++){
            int temp = sc.nextInt();
            temp = temp % 42;
            set.add(temp);
        }

        System.out.println(set.size());
        
    }
}
