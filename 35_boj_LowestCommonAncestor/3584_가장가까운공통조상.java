import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static int solution(int n, int[][] edge) {
        final int targetA = edge[n - 1][0];

        final int targetB = edge[n - 1][1];

        // 각 노드들의 부모를 기록한다. 초기 값은 -1
        int[] parent = new int[n + 1];
        Arrays.fill(parent, -1);

        for (int i = 0; i < n - 1; ++i) {
            parent[edge[i][1]] = edge[i][0]; // 자식[1]의 부모[0]를 기록
        }

        // 각 타겟의 깊이를 구한다
        // 부모가 루트가 아니면
        int targetA_depth = 1;
        int tmpA = targetA;
        int targetB_depth = 1;
        int tmpB = targetB;

        while (parent[tmpA] != -1) {
            tmpA = parent[tmpA];
            ++targetA_depth;
        }

        while (parent[tmpB] != -1) {
            tmpB = parent[tmpB];
            ++targetB_depth;
        }

        // 두 노드의 레벨을 맞춰준다
        tmpA = targetA;
        tmpB = targetB;
        if (targetA_depth < targetB_depth) {
            while (targetA_depth < targetB_depth) {
                targetB_depth--;
                tmpB = parent[tmpB]; // 부모로 올라감
            }
        } else if (targetB_depth < targetA_depth) {
            while (targetB_depth < targetA_depth) {
                targetA_depth--;
                tmpA = parent[tmpA];
            }
        }

        // 올라가면서, 같은 부모가 나타나면 최초 공통 부모이다
        // 현재 레벨에서 서로 다르다면, 부모로 올라간다
        while (tmpA != tmpB) {
            tmpA = parent[tmpA];
            tmpB = parent[tmpB];
        }
        // 탈출한 경우, targetA와 targetB가 같은 경우(최초 공통 부모)이다.
        return tmpA;

    }

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        int testCase = Integer.valueOf(br.readLine());

        for (int t = 0; t < testCase; ++t) {
            int n = Integer.valueOf(br.readLine());

            int[][] edge = new int[n][2];
            for (int i = 0; i < n; ++i) {
                // 마지막은 구하고자 하는 두 노드
                String[] tmp = br.readLine().split(" ");
                edge[i][0] = Integer.valueOf(tmp[0]); // 부모
                edge[i][1] = Integer.valueOf(tmp[1]); // 자식
            }

            bw.write(solution(n, edge) + "\n");

        }

        bw.flush();
        br.close();
        bw.close();
    }
}
