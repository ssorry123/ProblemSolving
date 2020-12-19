#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 100
vector< vector<int> > adj;
int N, K;

vector<bool> visited;
void dfs(int start) {
	visited[start] = true;
	for (int i = 0; i < adj[start].size(); ++i) {
		if (adj[start][i] > 0 && !visited[i]) {
			dfs(i);
		}
	}
}
int main(int argc, char** argv) {
	cin >> N;
	cin >> K;
	adj.assign(N, vector<int>(N));
	for (int i = 0; i < K; ++i) {
		int a, b;
		cin >> a >> b;
		adj[a - 1][b - 1] = 1;
		adj[b - 1][a - 1] = 1;
	}

	visited.assign(N, false);
	dfs(0);
	int cnt = 0;
	// 자기 자신은 제외, 자신이 퍼트린 사람 수 출력
	for (int i = 1; i < visited.size(); ++i)
		if (visited[i])
			++cnt;
	cout << cnt << endl;

	return 0;
}