#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define MAX 100001
int N, K;
typedef queue<pair<int, int> > Queue;
vector<bool> visited;

int main(int argc, char** argv) {
	cin >> N >> K;
	Queue q;
	// 현재 위치, 현재 시간
	q.push(make_pair(N, 0));

	int ret = 0;
	visited.assign(MAX, false);
	while (!q.empty()) {
		int here = q.front().first;     // 현재 위치
		int time = q.front().second;    // 현재 시간
		q.pop();
		visited[here] = true;

		// 동생을 만났다면
		if (here == K) {
			ret = time;
			break;
		}

		int go[3] = { here - 1, here + 1, 2 * here };
		for (int i = 0; i < 3; ++i)
			if (go[i] < MAX && go[i] >= 0 && !visited[go[i]])
				q.push(make_pair(go[i], time + 1));
	}

	cout << ret << endl;

	return 0;
}
