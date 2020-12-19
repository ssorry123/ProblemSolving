#include<iostream>
#include<vector>
#include<queue>
#include<climits>

#define MAX_V 20000

using namespace std;
// 디익스트라 알고리즘 사용
// 우선 순위 큐 사용
// BFS
 int main() {
    int V, E;	// 정점 개수, 간선 개수
    int K;		// 시작점 번호(1~V)
    cin >> V >> E;
    cin >> K;
    
    vector<int> dist(V+1, INT_MAX);	// 출발점부터 각 점까지 최단 거리 저장
    dist[K] = 0;					// 자신과 거리는 0

    // 간선 (u, v)의 가중치가 W일때 mat[u] = (W, v)
    vector< pair<int, int> > mat[MAX_V + 1];

    for (int i = 0; i < E; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        mat[u].push_back(make_pair(w, v));
    }

    // 가장 긴 거리가 우선순위가 되므로, 거리를 pq에 넣을때 -거리를 넣어주자
    // 가장 긴 거리가 -를 붙이면 가장 작아지므로 가장 우선순위가 낮다
    // 따라서 pq에서 pop을 하게되면 가장 작은 값이 나온다
    priority_queue< pair<int, int> > pq;
    pq.push(make_pair(0, K));	// 시작점에서 시작점까지의 최단거리 0

    while (!pq.empty()) {
        // 현재 위치 정보를 얻는다
        int here = pq.top().second;	// 현재 정점 번호
        int cost = -pq.top().first;	// 현재 정점까지 사용한 비용(최소 비용)
        pq.pop();

        if (dist[here] < cost) {
            // 여기까지 오는 비용보다 싼 비용이 이미 발견 되었다면
            // pq에서 제거된후 아무것도 안하고 다음 정점 검사
            // dist는 이미 최신으로 갱신되었고 갱신 후 인접 정점까지 거리도 다시 계산 했지만
            // 갱신 후 pq에서 비싼 비용을 제거하는 것이 까다롭기 때문
            continue;
        }

        // 현재 점과 인접한 점들을 검사한다
        for (int i = 0; i < (int)mat[here].size(); ++i) {
            int there = mat[here][i].second;			// 인접정점
            int candiDist = cost + mat[here][i].first;	// 현재 점까지 비용 + 현재점과 인접점의 거리

            if (candiDist < dist[there]) {
                // 새로 구한 비용이 기존에 구한 비용보다 쌀 경우
                dist[there] = candiDist;	// dist 갱신
                pq.push(make_pair(-candiDist, there));

            }
            else{
                // 초기 dist값은 MAX이므로 처음 방문하는 점들은 반드시 pq에 추가된다
                // 따라서 갈 수 있는 모든 점들을 방문한다
                // pq에 추가하지 않을 점은 이미 방문 한 상태이고, 더 짧은 거리를 찾지 못하였기 때문에
                // 인접한 점들을 다시 검사하지 않아도 된다
            }
        }

    }

    // c++ 출력시 endl대신 \n 을 사용할 것
    // 시간 초과의 원인

    for (int i = 1; i <= V; ++i) {
        if (dist[i] == INT_MAX) {
            cout << "INF" << "\n";
        }
        else {
            cout << dist[i] << "\n";
        }
    }

    return 0;
}