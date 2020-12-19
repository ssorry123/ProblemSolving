#include<iostream>

using namespace std;

int N;					// [2,11]
int arr[11] = { 0, };	// arr[i] -> [1,100]
int MIN = 1100000000;
int MAX = -MIN;
int p, m, t, d;

// 처음 dfs를 정의할때 반환값을 사용하지 않지만 그냥 int로 정의
// 그러나 시간 초과;;;;
// 반환을 int가 아닌 void로 해보니 시간 초과 해결
void dfs(int cnt, int ret);

int main() {
	cin >> N;
	for (int i = 0; i < N; ++i) {
		cin >> arr[i];
		// cout << arr[i] << ' ';
	}
	cin >> p >> m >> t >> d;

	dfs(0, arr[0]);

	cout << MAX << "\n" << MIN;

	return 0;
}

void dfs(int cnt, int ret) {
	if (cnt == N - 1) {
		if (ret > MAX)
			MAX = ret;
		if (ret < MIN)
			MIN = ret;
		return;
	}

	// 재귀호출 할때마다 고를 수 있는 연산기호를 고른다
	int t_ret;
	if (p > 0) {
		--p;
		t_ret = ret + arr[cnt + 1];
		dfs(cnt + 1, t_ret);
		++p;
	}
	if (m > 0) {
		--m;
		t_ret = ret - arr[cnt + 1];
		dfs(cnt + 1, t_ret);
		++m;
	}
	if (t > 0) {
		--t;
		t_ret = ret * arr[cnt + 1];
		dfs(cnt + 1, t_ret);
		++t;
	}
	if (d > 0) {
		--d;
		if (ret < 0) {
			t_ret = -ret;
			t_ret = -(t_ret / arr[cnt + 1]);
			dfs(cnt + 1, t_ret);
		}
		else {
			t_ret = ret / arr[cnt + 1];
			dfs(cnt + 1, t_ret);
		}
		++d;
	}
}