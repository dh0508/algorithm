import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        if (N%2 == 0){
            System.out.println("I LOVE CBNU");
        }else{
            for (int i = 1; i <= N; i++) {
                System.out.printf("*");
            }
            System.out.println();
            for (int i = 1; i <= N/2+1; i++) {
                if (i == 1){
                    for (int j = 1; j <= (N-1)/2; j++) {
                        System.out.printf(" ");
                    }
                    System.out.printf("*");
                    System.out.println("");
                }else {
                    for (int j = 1; j<= (N-2*(i-1)+1)/2-1; j++){
                        System.out.printf(" ");
                    }
                    System.out.printf("*");
                    for (int j = 1; j <= 2*(i-1)-1; j++){
                        System.out.printf(" ");
                    }
                    System.out.printf("*");
                if (i != N/2+1)
                    System.out.println("");
                }

            }
        }
    }
}
