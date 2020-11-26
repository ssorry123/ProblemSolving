import java.util.Scanner;

class Solution {
    public static void printStarN(int n) {
        for (int i = 0; i < n; ++i)
            System.out.print("*");
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        for (int i = 0; i < b; ++i) {
            printStarN((a));
        }
    }
}