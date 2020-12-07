import java.util.Arrays;
import java.util.PriorityQueue;

// 1번 마을에서,
// 각 마을까지 K의 비용으로 갈 수 있는 마을의 개수 세기
// 디익스트라

class Item implements Comparable<Item> {
    Integer here;
    Integer cost; // 1의 위치에서, here까지 걸린 비용

    Item(Integer here, Integer cost) {
        this.here = here;
        this.cost = cost;
    }

    @Override
    public int compareTo(Item o) {
        // TODO Auto-generated method stub
        return cost.compareTo(o.cost);
    }

}

class Solution {
    public int solution(int N, int[][] road, int K) {

        // 각 마을에서, 다른 마을까지 최소 거리
        int[][] dist = new int[N + 1][N + 1];
        // 초기 값은 무한
        for (int[] arr : dist) {
            Arrays.fill(arr, Integer.MAX_VALUE);
        }
        for (int[] arr : road) {
            int a = arr[0];
            int b = arr[1];
            int d = Math.min(arr[2], dist[a][b]);
            dist[a][b] = dist[b][a] = d;
        }

        System.out.println(1);
        // bfs, 다익스트라
        PriorityQueue<Item> pq = new PriorityQueue<>(); // java 기본 작은값 먼저
        // 마을 1번부터 마을 1까지 비용은 0;
        int[] ret = new int[N + 1];
        Arrays.fill(ret, Integer.MAX_VALUE);
        ret[1] = 0;
        pq.add(new Item(1, 0));

        while (!pq.isEmpty()) {
            Item me = pq.poll();
            int here = me.here;
            int cost = me.cost;

            // 이미 here까지 구했었다면,
            if (ret[here] < cost) {
                continue;
            }

            // 인접한 마을 검사
            for (int next = 1; next <= N; ++next) {
                // 연결 되어 있다면
                if (dist[here][next] < Integer.MAX_VALUE) {
                    // 그리고, 새로 구하는 비용이 더 싸다면
                    int newCost = cost + dist[here][next];
                    if (newCost < ret[next]) {
                        ret[next] = newCost; // next지점까지 최소 비용 갱신
                        // next지점과 연결된 지점 다시 계산하기 위해 큐에 넣어줌
                        pq.add(new Item(next, newCost));
                    }
                }
            }

        }

        int answer = 0;
        
        for (int i = 1; i <= N; ++i) {
            if (ret[i] <= K) {
                ++answer;
            }
        }
        return answer;
    }
}
