import java.util.*;

class Solution {

    public static int solution(int[] arr) {
        double avg = 0;

        for (int a : arr) {
            avg += a;
        }

        avg = Math.round(avg / arr.length);

        return (int) avg;
    }

    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        /*
         * 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
         */

        for (int test_case = 1; test_case <= T; test_case++) {
            int[] arr = new int[10];
            for (int i = 0; i < 10; ++i) {
                arr[i] = sc.nextInt();
            }
            System.out.printf("#%d %d\n", test_case, solution(arr));

        }

        sc.close();
    }
}