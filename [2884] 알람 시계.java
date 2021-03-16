import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int hour = scan.nextInt();
        int minute = scan.nextInt();

        minute = minute - 45;

        if (minute < 0){
            hour -= 1;
            minute += 60;
        }

        if (hour < 0){
            hour += 24;
        }

        System.out.printf("%d %d",hour,minute);

    }
} 
