#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 25
vector< vector<int> > adj;
int arr[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
int N;

bool check(int r, int c) {
	if (r >= N || r < 0 || c >= N || c < 0)
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
	cin >> N;
	adj.assign(N, vector<int>(N));
	char str[MAX + 1];
	for (int i = 0; i < N; ++i) {
		scanf("%s", str);
		for (int j = 0; j < N; ++j) {
			adj[i][j] = str[j] - 48;
		}
	}

	vector<int> ret;
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			if (check(i, j))
				ret.push_back(dfs(i, j));
			
	sort(ret.begin(), ret.end());
	cout << ret.size() << endl;
	for (int i = 0; i < ret.size(); ++i)
		printf("%d\n", ret[i]);

	return 0;
}