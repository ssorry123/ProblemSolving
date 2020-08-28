#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
int N;
int arr[1000];
vector<int> right_cache;
vector<int> left_cache;

// idx부터 오른쪽으로 감소하는 부분수열의 최대 길이
int dfs_right(int idx) {
	if (right_cache[idx] != -1)
		return right_cache[idx];

	int ret = 1;	// 자기 자신의 길이
	for (int i = idx + 1; i < N; ++i) {
		int tmp_ret;
		if (arr[i] < arr[idx]) {
			tmp_ret = 1 + dfs_right(i);
			ret = max(tmp_ret, ret);
		}
	}
	right_cache[idx] = ret;
	return ret;
}
// idx부터 왼쪽으로 감소하는 부분수열의 최대 길이
int dfs_left(int idx) {
	if (left_cache[idx] != -1)
		return left_cache[idx];

	int ret = 1;	// 자기 자신의 길이
	for (int i = idx - 1; i >= 0; --i) {
		int tmp_ret;
		if (arr[i] < arr[idx]) {
			tmp_ret = 1 + dfs_left(i);
			ret = max(tmp_ret, ret);
		}
	}
	left_cache[idx] = ret;
	return ret;
}


int main(int argc, char** argv) {
	cin >> N;
	for (int i = 0; i < N; ++i)
		scanf("%d", &arr[i]);

	left_cache.assign(1000, -1);
	for (int i = 0; i < N; ++i)
		dfs_left(i);

	right_cache.assign(1000, -1);
	for (int i = 0; i < N; ++i)
		dfs_right(i);

	int ret = 0;
	for (int i = 0; i < N; ++i) {
		// arr[i]를 포함하는 왼쪽 부분수열과 오른쪽 부분수열
		int tmp_ret = left_cache[i] + right_cache[i] - 1;
		ret = max(ret, tmp_ret);
	}
	cout << ret << endl;

	return 0;
}