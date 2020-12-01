import java.util.Arrays;

class Dfs {
    // 맵의 크기를 받음
    private int m;
    private int n;
    // 방문한 지역을 기록
    public boolean[][] visited;

    // 생성자
    Dfs(int m, int n) {
        this.m = m;
        this.n = n;
        visited = new boolean[m][n];
        for (int i = 0; i < m; ++i)
            Arrays.fill(visited[i], false);
    }

    // 범위 체크
    private boolean check(int r, int c) {
        if (r >= m || r < 0 || c >= n || c < 0)
            return false;
        return true;
    }

    // r, c를 시작으로 퍼져나가는 영역의 수를 구한다
    public int dfs(int r, int c, int[][] picture) {
        visited[r][c] = true; // 방문 표시
        int val = picture[r][c];

        int ret = 1; // 자기 자신 방문

        final int dr[] = { 0, 0, -1, 1 };
        final int dc[] = { -1, 1, 0, 0 };
        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            // 범위를 넘어가지 않고, 방문하지 않았다면, 그리고 같은 영역이라면
            if (check(nr, nc) && !visited[nr][nc] && picture[nr][nc] == val) {
                ret += dfs(nr, nc, picture);
            }
        }

        return ret;
    }
}

class Solution {

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        Dfs dfs = new Dfs(m, n);
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                // 0은 영역이 아니다 ( 색깔이 아니다 ), 방문하지 않은 지역이라면
                if (!dfs.visited[r][c] && picture[r][c] != 0) {
                    int ret = dfs.dfs(r, c, picture);
                    // System.out.println(ret);
                    ++numberOfArea;
                    maxSizeOfOneArea = Math.max(ret, maxSizeOfOneArea);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}