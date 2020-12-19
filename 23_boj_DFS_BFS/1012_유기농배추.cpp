#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 50
vector< vector<int> > adj;
int arr[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
int M, N;

bool check(int r, int c) {
	if (r >= M || r < 0 || c >= N || c < 0)
		return false;
	if (adj[r][c] == 2 || adj[r][c] == 0)
		return false;
	if (adj[r][c] == 1)
		return true;
	return false;
}

int dfs(int r, int c) {
	adj[r][c] = 2;
	int ret = 1;
	for (int i = 0; i < 4; ++i) {
		int next_r, next_c;
		next_r = r + arr[i][0];
		next_c = c + arr[i][1];
		if (check(next_r, next_c))
			ret += dfs(next_r, next_c);
	}
	return ret;
}

int main(int argc, char** argv) {
	int testCase;
	cin >> testCase;
	for (int t = 0; t < testCase; ++t) {
		int K;
		cin >> M >> N >> K;
		adj.assign(M, vector<int>(N, 0));
		int a, b;
		for (int i = 0; i < K; ++i) {
			scanf("%d %d", &a, &b);
			adj[a][b] = 1;
		}
		int ret = 0;
		for (int r = 0; r < M; ++r)
			for (int c = 0; c < N; ++c)
				if (check(r, c)) {
					dfs(r, c);
					++ret;
				}
		cout << ret << endl;
	}

	return 0;
}