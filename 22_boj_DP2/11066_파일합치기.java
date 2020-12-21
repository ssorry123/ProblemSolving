import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    // 메모이제이션
    static int[][] dp; // 범위의
    // 인접한 두 카드를 합칠때
    // 한 카드가 여러 카드였을 수도 있으므로, 그 카드들의 비용은 다시 더해진다.
    static int[] sum;

    // left ~ right 까지 카드들을 합치는 비용
    public static int divide(int left, int right, int[] arr) throws IOException {
        // 이미 구한 적이 있는 범위인 경우
        if (dp[left][right] != -1) {
            return dp[left][right];
        }
        // 범위가 1인 경우
        if (left == right) {
            return dp[left][right] = 0;
        }
        // 범위가 2인 경우
        if (left + 1 == right) {
            return dp[left][right] = arr[left] + arr[right];
        }

        // 분할
        int ret = Integer.MAX_VALUE;
        for (int mid = left; mid < right; ++mid) {
            int a = divide(left, mid, arr);
            int b = divide(mid + 1, right, arr);

            // 3장 이상의 카드가 두장의 카드가 된 후에,
            // 2장이 된 카드가 합쳐지는데 발생하는 비용
            ret = Math.min(ret, a + b);
        }

        // 3장 이상의 카드가 2장이 된 후에
        // 2장이 된 카드가 합쳐지는 비용만 계산한 ret이므로
        // 2장이 되기 전까지 합쳐졌던 비용들을 더해주어야 함
        /*
         * ex) 40, 30, 30, 50
            70(40+30), 80(30+50)
            150(40+30+30+50)
         * 
         * answer = 70 + 80 + 150 = 300
         * 
         * ex) 1, 1, 1
            2(1+1), 1(0)
               3(1+1+1)
         * 
         * answer = 2 + 0 + 3 = 5
         */

        return dp[left][right] = ret + sum[right + 1] - sum[left];
    }

    public static void solution(int K, int[] arr) throws IOException {
        int left = 0;
        int right = arr.length - 1; // K-1

        int answer = divide(left, right, arr);
        bw.write(answer + "\n");
    }

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; ++i) {
            int K = Integer.parseInt(br.readLine()); // 소설 장의 수
            int[] arr = new int[K];

            int idx = 0;
            sum = new int[K + 1];
            sum[0] = 0;
            int sumVal = 0;
            for (String s : br.readLine().split(" ")) {
                arr[idx] = Integer.parseInt(s);
                sum[idx + 1] = sum[idx] + arr[idx];
                idx++;
            }
            // System.out.println(Arrays.toString(arr));

            // dp 초기화
            dp = new int[K][K];
            for (int[] d : dp)
                Arrays.fill(d, -1);

            solution(K, arr);
        }

        bw.flush();
        br.close();
        bw.close();
    }
}