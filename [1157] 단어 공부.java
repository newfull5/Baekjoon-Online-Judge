import java.util.HashMap;
import java.util.Scanner;
import java.util.Set;

public class Main{
    public static void main(String[] args){
        // Create Hash Map Object
        HashMap<String, Integer> diction = new HashMap<>();

        // Create Scanner Object
        Scanner sc = new Scanner(System.in);

        // get Input
        String str = sc.nextLine();

        // Make all letters to Capital
        str = str.toUpperCase();

        // Change String to array 
        // to find to most frequent letter
        String[] strarr = str.split("");
        
        for (int i = 0; i < strarr.length; i++){
            String letter = strarr[i];

            if (diction.get(letter) == null){
                diction.put(letter, 1);
            }
            else{
                diction.put(letter, diction.get(letter) + 1);
            }
        }

        // Example)
        // inputs = "ABCAA",
        // diction = {A=3, B=1, C=1}

        int most = 0;
        String answer = "";

        Set<String> sets = diction.keySet();

        for (String s : sets){
            int temp = diction.get(s);
            if (temp > most){
                answer = s;
                most = temp;
            }
        }
        
        int cnt = 0;
        
        // check if the most is not unique
        for (int n : diction.values()){
            if (n == most){
                cnt += 1;
            }
            if (cnt == 2){
                break;
            }
        }

        if (cnt == 2){
            System.out.println("?");
        }
        else{
            System.out.println(answer);
        }
        
    }
}
