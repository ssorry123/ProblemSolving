#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;
#define MAX 20000
bool adj[MAX + 1][MAX + 1];
vector<int> dist;
int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    // 무방향 그래프이다
    for (int i = 0; i < edge.size(); ++i) {
        adj[edge[i][0]][edge[i][1]] = true;
        adj[edge[i][1]][edge[i][0]] = true;
    }
    // 해당 노드에도착했을때 거리 기록, 초기화 -1
    dist.assign(n + 1, -1);
    // 1번부터 어떤 노드까지의 거리중 최대값
    int d_max = -1;
    // bfs를 위한 큐
    queue<pair<int, int> > q;
    // 시작점 1에서 1까지 거리는 0
    q.push(make_pair(1, 0));
    dist[1] = 0;
    while (!q.empty()) {
        int here = q.front().first;
        int d = q.front().second;
        d_max = d;
        q.pop();
        int n_d = d + 1;
        for (int i = 1; i <= n; ++i) {
            // 연결되어있다면, 그리고 방문하지 않은 노드라면
            if (adj[here][i] && dist[i] == -1) {
                q.push(make_pair(i, n_d));
                dist[i] = n_d;
            }
        }
    }
    for (int i = 1; i <= n; ++i)
        if (dist[i] == d_max)
            answer++;


    return answer;
}