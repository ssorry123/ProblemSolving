#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
#define MAX 500	// 전깃줄을 연결할 수 있는 index
int N;			// 전깃줄의 개수 <= 100

vector<int> cache;
vector<int> A;
int dfs(int idx) {
	if (cache[idx] != -1)
		return cache[idx];

	int ret = 1;
	for (int i = idx + 1; i < A.size(); ++i) {
		if (A[i] > A[idx]) {
			ret = max(ret, 1 + dfs(i));
		}
	}
	return cache[idx] = ret;
}

vector<int> tmp;
int main(int argc, char** argv) {
	cin >> N;
	// A배열의 원소들이 증가하는 수열이어야 함
	// 가장 긴 증가하는 부분수열을 만들면 가장 적게 전깃줄 제거

	int a, b;
	tmp.assign(MAX, -1);
	for (int i = 0; i < N; ++i) {
		scanf("%d %d", &a, &b);
		tmp[a - 1] = b;
	}
	for (int i = 0; i < tmp.size(); ++i) {
		if (tmp[i] != -1)
			A.push_back(tmp[i]);
	}

	cache.assign(MAX, -1);
	int ret = 0;
	for (int i = 0; i < N; ++i)
		ret = max(ret, dfs(i));
	cout << N - ret << endl;

	return 0;
}