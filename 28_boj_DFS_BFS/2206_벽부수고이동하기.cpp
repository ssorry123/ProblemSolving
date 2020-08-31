#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define MAX 1000
int N, M;
char map[MAX][MAX + 1];	// %s 입력시 마지막 문자를 위한 공간
// (메모리 절약을 위해 bool로 방문 여부만)
bool dist0[MAX][MAX];	// 벽을 부수기 전 해당 지점까지 최단 이동 거리
bool dist1[MAX][MAX];	// 벽을 부순 후 해당 지점까지 최단 이동 거리(벽을 더이상 부술 수 있는 기회가 없음)
// BFS, cost는 시작지점에서 해당 지점까지 패킷이 이동하는데 걸린 비용이며, 시간축에 해당

// 벽을 부수기 전 패킷이 dist0에 기록하고, 벽을 부순 후 패킷이 dist1에 기록하게 되면
// dist0에 방문하였다고 기록한 지점을 다시 방문하게 될 수도 있다(왔던 길을 되돌아 가는 탐색을 하게 될 수도 있다.)
// 그러나 BFS이고, 더이상 벽을 부술 수 있는 기회따위는 없으므로, 그 지점에서 bfs로 목적 지점에 최단으로 도달하는 것은 명백함.

// 만약 처음으로 벽을 부순 패킷 이후에 또 벽을 부순 패킷들이 나타나게 되면 그 패킷들도 dist1을 참고하게 된다.
// dist1을 참고하는데, 이미 다른 패킷이 해당 지점에 기록하였을 경우, 해당 지점에서 목적지까지 최단 거리는
// 전에 그 지점을 방문했던 패킷이 먼저 찾아내게 되므로,(bfs는 한점을 중심으로 퍼져나가고, 한점을 중심으로 cost가 커지므로)
// 어떤 패킷이 dist1의 한 지점을 방문한 후 또 같은 지점을 방문하는 패킷들은
// 더이상 쓸모가 없다.(해당 지점을 먼저 발견한 패킷이 시작한 시간(cost)이 빠르므로 목적지에 먼저 도착하게 된다)
// 그러나 dist1의 어떤 지점에 어떤 패킷도 기록하지 않은 경우 그 지점을 시작으로 최단거리를 찾을 가능성이 있다.

// 맵을 움직이는 가상의 패킷
typedef struct _LOC {
    // 패킷의 위치
    int r;
    int c;
    // 해당 위치까지 비용
    int cost;
    // 다음 위치로 이동할 때 벽을 부술 수 있는지 여부
    bool can_break;
}LOC;
//struct compare {
//	bool operator()(LOC &a, LOC &b){
//		return a.cost > b.cost;
//	}
//};
//priority_queue<LOC, vector<LOC>, compare> q;


bool check(int r, int c);
typedef queue<LOC> Q_LOC;
Q_LOC q;
int bfs() {
    // 시작 위치, 큐에 삽입
    q.push({ 0, 0, 1, true });
    // dist에 기록
    dist0[0][0] = 1;


    int arr[4][2] = { {0, 1}, {0, -1}, {-1, 0}, {1, 0} };
    while (!q.empty()) {
        // 확인할 원소 pop
        LOC me = q.front();
        q.pop();

        // 목적지 도착한 경우
        if (me.r == N - 1 && me.c == M - 1)
            return me.cost;

        // 다음 cost
        int n_cost = me.cost + 1;
        for (int i = 0; i < 4; ++i) {
            // 다음 위치
            int n_r = me.r + arr[i][0], n_c = me.c + arr[i][1];
            // 다음 위치가 맵을 벗어나지 않고
            if (check(n_r, n_c)) {
                // 벽을 부순 패킷들 또는 부수게 되는 패킷들은 dist1을 참고한다
                // 벽을 부시지 않은 패킷들은 dist0을 참고한다
                char next = map[n_r][n_c];

                // 벽을 부순 패킷은 벽이아니고, 방문하지 않은 점만 방문할 수 있다
                if (!me.can_break && dist1[n_r][n_c] == 0 && next == '0') {
                    q.push({ n_r, n_c, n_cost, false });
                    dist1[n_r][n_c] = n_cost;
                }
                // 벽을 아직 부수지 않은 패킷이
                else if (me.can_break) {
                    // 벽이 아니고, 아직 방문하지 않았을때
                    if (next == '0' && dist0[n_r][n_c] == 0) {
                        q.push({ n_r, n_c, n_cost, true });
                        dist0[n_r][n_c] = 1;
                    }
                    // 벽인데, 어떤 패킷도 먼저 방문하지 않았을때
                    else if(next == '1' && dist1[n_r][n_c] == 0) {
                        q.push({ n_r, n_c, n_cost, false });
                        dist1[n_r][n_c] = 1;
                    }
                }
            }
        }
    }
    return -1;
}
int main(int argc, char** argv) {
    cin >> N >> M;

    for (int i = 0; i < N; ++i) {
        scanf("%s", &map[i]);
    }
    cout << bfs() << endl;

    return 0;
}

bool check(int r, int c) {
    if (r < 0 || c < 0 || r >= N || c >= M)
        return false;
    return true;
}