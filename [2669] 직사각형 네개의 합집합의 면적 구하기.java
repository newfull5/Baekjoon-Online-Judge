import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] squares = new int[4][4];
        int max_x = 0;
        int max_y = 0;

        for (int i = 0; i<4; i++){
            for (int j = 0; j<4; j++){
                squares[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i<4; i++){
            if (squares[i][2] > max_x){
                max_x = squares[i][2];
            }

            if (squares[i][3] > max_y){
                max_y = squares[i][3];
            }
        }

        int[][] matrix = new int[max_x][max_y];

        for (int i = 0; i <4; i++){
            int x = squares[i][0];
            int y = squares[i][1];
            int _x = squares[i][2];
            int _y = squares[i][3];

            for (int x_=x; x_<_x; x_++){
                for (int y_=y; y_<_y; y_++){
                    matrix[x_][y_] = 1;
                }
            }
        }

        int answer = 0;

        for (int i =0; i<max_x; i++){
            for (int j = 0; j<max_y; j++){
                if (matrix[i][j] == 1){
                    answer += 1;
                }
            }
        }

        System.out.println(answer);
    }    
}
