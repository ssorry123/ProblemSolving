#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define MAX 1000
int adj[MAX][MAX];
int N, M;		// row수, col수
int cnt_0 = 0;	// 익지 않은 토마토 수

bool check(int r, int c);

// 레벨이 day인 토마토(r, c) 근처에 있는 안 익은 토마토들을
// 익은 토마토로 바꾸고, 레벨이 day+1인 토마토를 저장하는 큐에 추가한다
void bfs(int r, int c, queue< pair<int, int> >& q) {
	int arr[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
	for (int i = 0; i < 4; ++i) {
		int next_r, next_c;
		next_r = r + arr[i][0];
		next_c = c + arr[i][1];
		// 익게 만들 수 있는 토마토인 경우
		if (check(next_r, next_c)) {
			adj[next_r][next_c] = 1;			// 익게 만든다
			q.push(make_pair(next_r, next_c));	// 큐에 추가
			--cnt_0;							// 익지 않은 토마토 수 제거
		}
	}
}

int main(int argc, char** argv) {
	// col수, row수
	cin >> M >> N;
	int tmp;
	// 0일차에 익어있는 토마토들
	queue<pair<int, int> > q_today;
	for (int r = 0; r < N; ++r)
		for (int c = 0; c < M; ++c) {
			scanf("%d", &tmp);
			adj[r][c] = tmp;
			if (tmp == 0)
				++cnt_0;
			if (tmp == 1)
				q_today.push(make_pair(r, c));
		}
	// 모든 토마토가 익어있다면(익지 않은 토마토가 한개도 없다면)
	if (cnt_0 == 0)
		cout << 0 << endl;
	else {
		int day = 0;
		while (true) {
			// day+1 큐 생성
			queue<pair<int, int> > q_tomorrow;
			while (!q_today.empty()) {
				// today에 익어있는 토마토들
				pair<int, int> me = q_today.front();	
				q_today.pop();
				int me_r = me.first, me_c = me.second;
				// 자신 주변의 토마토들을 익게 만든 후, tomorrow 큐에 추가한다
				bfs(me_r, me_c, q_tomorrow);
			}
			// tomorrow에 아무런 토마토를 만들지 못한 경우
			if (q_tomorrow.empty())
				break;
			// 다음날!
			q_today = q_tomorrow;
			++day;
		}
		if (cnt_0 > 0)
			cout << -1 << endl;
		else
			cout << day << endl;
	}

	return 0;
}

bool check(int r, int c) {
	if (r >= N || r < 0 || c >= M || c < 0)
		return false;
	// 처음부터 익지 않은 토마토인 경우
	if (adj[r][c] == 0)
		return true;
	// 그 외 모든 경우 false
	return false;
}
