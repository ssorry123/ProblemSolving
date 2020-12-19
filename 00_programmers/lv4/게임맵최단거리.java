// 왜 4단계인지 모르겠다.

import java.util.*;

class Solution {
    int[][] maps;
    int R;
    int C;

    class Node {
        int r;
        int c;
        int cost;

        Node(int r, int c, int cost) {
            this.r = r;
            this.c = c;
            this.cost = cost;
        }

        void print() {
            System.out.println(r + " " + c + " " + cost);
        }
    }

    public int solution(int[][] MAP) {

        maps = MAP;
        R = maps.length;
        C = maps[0].length;

        // bfs

        boolean[][] visited = new boolean[R][C];
        for (boolean[] v : visited) {
            Arrays.fill(v, false);
        }

        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(0, 0, 1));
        visited[0][0] = false;

        int[][] drc = new int[][] { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

        while (!queue.isEmpty()) {
            Node here = queue.poll();

            if (here.r == R - 1 && here.c == C - 1)
                return here.cost;

            for (int[] d : drc) {
                int nr = here.r + d[0];
                int nc = here.c + d[1];

                if (nr < 0 || nc < 0 || nr >= R || nc >= C)
                    continue;
                if (visited[nr][nc])
                    continue;
                if (maps[nr][nc] == 0)
                    continue;

                visited[nr][nc] = true;
                queue.add(new Node(nr, nc, here.cost + 1));

            }

        }

        return -1;
    }
}