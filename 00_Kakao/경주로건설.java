/*
 * 공개된 많은 풀이들이 틀렸을수도 있는 문제
 * 
 * 대부분
 * + bfs
 * + 새로운 저렴한 경로를 찾은 경우 다시 방문 가능
 * + 저렴하지 않을 경우 무시
 * 하는 방법으로, 약간 다익스트라 같이 풀었다.
 * 
 * 하지만 아래와 같은 케이스 가능
 * 1)
 *             1
 *             2
 *       1-2-3 3-9(도착지)
 * 2)   
 *             1
 *             2
 *             x
 *       1-2-3-4-5(도착지)
 *              
 * 1) 위에서 내려오다가 오른쪽으로 꺽어 가는 경우 비용은 9이다.
 * 2) 왼쪽에서 오른쪽으로 직진만 하는 경우 비용은 5이다.
 * 
 * 하지만 교차하는 지역을 방문할때
 * 1)의 경우 비용은 항상 3이고
 * 2)의 경우 비용은 항상 4이므로 1)에 의해 올바른 정답인 2)가 씹힌다.
 * 1)과 2)의 교차 지역 비용이 같더라도, 둘중에 하나는 씹힌다.
 * 
 * 즉 교차지역에서 그 당시엔 비용이 클지 몰라도, 나중에는 보니 더 저렴한 비용이었다는 것..
 * 
 * 따라서 어떠한 지점을 방문할때 비용은
 * 그 지점을 방문할때 어떠한 방향으로 방문하였는지에 따라 모두 다르게 저장해주어야 한다.
 * 즉,, 위,아래,왼쪽,오른쪽으로 어떠한 지점을 방문한 비용을 따로 저장해주어야 한다.
 */

import java.util.*;

class Solution {

    class Packet implements Comparable<Packet> {
        int r;  // row 위치
        int c;  // col 위치
        Integer cost;
        String point;

        /**
         * @param up, down, left, right
         * @return 올바르지 않을 경우 -1, 올바를 경우 int 매핑
         */
        public int getPointNum(String s) {
            if (s.equals("up"))
                return 0;
            else if (s.equals("down"))
                return 1;
            else if (s.equals("left"))
                return 2;
            else if (s.equals("right"))
                return 3;
            else
                return -1;
        }

        Packet(int r, int c, int cost, String point) {
            this.r = r;
            this.c = c;
            this.cost = cost;
            this.point = point;
        }

        // 우선순위큐 사용하기 위한
        @Override
        public int compareTo(Packet p) {
            return cost.compareTo(p.cost);
        }

        /**
         * 확인용
         */
        public void print() {
            System.out.println(r + " " + c + " " + cost + " " + point);
        }
    }

    public int solution(int[][] board) {
        int answer = 0;
        int n = board.length;

        // 한지점에서 목표지점까지 최소 비용은 한가지로 정해져 있다.
        // 모든 방향성마다 다른 거리값을 가지고 있어야 한다.
        int[][][] dist = new int[4][n][n];
        for (int[][] d : dist) {
            for (int[] arr : d) {
                Arrays.fill(arr, Integer.MAX_VALUE);
            }
        }

        PriorityQueue<Packet> pq = new PriorityQueue<>();
        dist[0][0][0] = dist[1][0][0] = dist[2][0][0] = dist[3][0][0] = 0;
        if (board[0][1] == 0) {
            pq.add(new Packet(0, 1, 1, "right"));
            dist[3][0][1] = 1;
        }
        if (board[1][0] == 0) {
            pq.add(new Packet(1, 0, 1, "down"));
            dist[1][1][0] = 1;
        }

        // up 0, down 1, left 2, right 3
        String[] point = new String[] { "up", "down", "left", "right" };
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (!pq.isEmpty()) {
            Packet here = pq.poll();
            int herePoint = here.getPointNum(here.point);
            // here.print();
            
            if(here.r == n-1 && here.c == n-1){
                break;
            }

            // 이미 다른 패킷이 최소 비용을 갱신해놓았다면 무시함
            if (dist[herePoint][here.r][here.c] < here.cost) {
                continue;
            }

            // 역방향 구하기, 역방향으로만 안가면 됨
            // 역방향 자동으로 걸러지지만, 약간의 최적화
            int hereReversePoint = (herePoint % 2 == 0 ? herePoint + 1 : herePoint - 1);

            for (int i = 0; i < 4; ++i) {
                int nr = here.r + dr[i];
                int nc = here.c + dc[i];

                if (i == hereReversePoint) {
                    continue;
                }
                if (nr < 0 || nc < 0 || nr >= n || nc >= n) {
                    continue;
                }
                if (board[nr][nc] == 1) {
                    continue;
                }

                String nPoint = point[i];
                int addCost = (here.point == nPoint ? 1 : 6);
                if (dist[i][nr][nc] >= here.cost + addCost) {
                    dist[i][nr][nc] = here.cost + addCost;
                    pq.add(new Packet(nr, nc, dist[i][nr][nc], nPoint));
                }
            }

        }

        answer = Math.min(dist[0][n - 1][n - 1], dist[1][n - 1][n - 1]);
        answer = Math.min(answer, dist[2][n - 1][n - 1]);
        answer = Math.min(answer, dist[3][n - 1][n - 1]);
        answer *= 100;
        System.out.println(answer);
        return answer;
    }
}