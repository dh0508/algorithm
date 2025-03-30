import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int c = 100;
        int s = 100;
        for (int i = 0;i < n; i++){
            int cdice = scanner.nextInt();
            int sdice = scanner.nextInt();
            if (cdice > sdice){
                s -= cdice;
            } else if (cdice < sdice) {
                c -= sdice;


            }
        }
        System.out.println(c);
        System.out.println(s);
    }
}
