import java.io.*;
import java.util.*;

// 더 이상 사용되지 않는 값을 버림으로써 공간 복잡도를 향상시키는 문제. 메모리 제한에 주목하세요.
// 4MB 제한
// 이라지만 그냥 해도 메모리 제한에 걸리진 않았다.
// 다른 언어는 모르겠음.


public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    // 메모리 절약 버전. 11680KB
    public static void solution(int[] coins, int n, int k) throws IOException {
        if (coins.length != n + 1) {
            System.out.println("wrong input");
            return;
        }

        // 동전 가치순으로 정렬
        Arrays.sort(coins);

        int[] dp = new int[k + 1];

        // 모든 코인들은 0개 사용해서 '0'을 만들 수 있음
        dp[0] = 1;

        for (int a = 1; a <= n; ++a) {
            // a번째 코인 가치
            int coinA = coins[a];

            for (int b = 1; b <= k; ++b) {
                // 이러나 저러나 dp[a-1][b]는 dp[a][b]=0 에 더해진다.
                // 하나의 (a,b)에 대해서, b-coinA는 중복될 일이 없다
                // (한번씩만 쓰고 다시 찾지 않는다)
                if (coinA <= b)
                    dp[b] = dp[b] + dp[b - coinA];
                else
                    dp[b] = dp[b];
            }
        }

        bw.write(String.valueOf(dp[k]));

    }

    // 메모리 초과 버전인데 통과함;ㅋㅋㅋㅋㅋㅋㅋ
    // 15920KB
    public static void solution1(int[] coins, int n, int k) throws IOException {
        if (coins.length != n + 1) {
            System.out.println("wrong input");
            return;
        }

        // 동전 가치순으로 정렬
        Arrays.sort(coins);

        // dp[a][b] = a번째 동전까지 사용해서, 총 금액 'b'를 만들 수 있는 경우의 수
        int[][] dp = new int[n + 1][k + 1];

        // 모든 코인들은 0개 사용해서 '0'을 만들 수 있음
        for (int r = 0; r <= n; ++r) {
            dp[r][0] = 1;
        }

        for (int a = 1; a <= n; ++a) {
            // a번째 코인 가치
            int coinA = coins[a];

            for (int b = 1; b <= k; ++b) {

                // 현재 코인의 가치가 목표인 'b'보다 작다면
                if (coinA <= b) {
                    dp[a][b] += dp[a - 1][b]; // a-1번째 코인까지로 만든 목표 'b'
                    dp[a][b] += dp[a][b - coinA]; // a번째 코인까지로 만든 목표 'b' - 'coinA'
                }
                // 현재 코인의 가치가 'b'보다 크다면
                else {
                    dp[a][b] = dp[a - 1][b];
                }

            }
        }

        bw.write(String.valueOf(dp[n][k]));
    }

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        String[] tmp = br.readLine().split(" ");
        int n = Integer.parseInt(tmp[0]);
        int k = Integer.parseInt(tmp[1]);

        // 0의 가치를 가지는 코인도 추가, 총 코인의 개수 n+1개
        int[] coins = new int[n + 1];
        for (int i = 1; i <= n; ++i) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        // solution(coins, n, k);
        solution1(coins, n, k);

        bw.flush();
        br.close();
        bw.close();
    }
}
