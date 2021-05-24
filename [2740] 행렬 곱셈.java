import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int [][] matrix1 = new int[n][m];
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                matrix1[i][j] = sc.nextInt();
            }
        }

        m = sc.nextInt();
        int k = sc.nextInt();

        int [][] matrix2 = new int[m][k];

        for (int i = 0; i < m; i++){
            for (int j = 0; j < k; j++){
                matrix2[i][j] = sc.nextInt();
            }
        }

        int [][] answer = new int [n][k];

        for (int i=0; i<n; i++){
            for(int j=0; j<k; j++){
                for(int l=0; l<m; l++){
                    answer[i][j] += matrix1[i][l]*matrix2[l][j];
                }
            }
        }

        for (int i=0; i<n; i++){
            for (int j=0; j<k; j++){
                System.out.print(answer[i][j]);
                System.out.print(' ');
            }
            System.out.println();
        }
    }    
}
