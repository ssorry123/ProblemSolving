#include<iostream>

using namespace std;

int N;					// [2,11]
int arr[11] = { 0, };	// arr[i] -> [1,100]
int MIN = 1100000000;
int MAX = -MIN;
int p, m, t, d;

// ó�� dfs�� �����Ҷ� ��ȯ���� ������� ������ �׳� int�� ����
// �׷��� �ð� �ʰ�;;;;
// ��ȯ�� int�� �ƴ� void�� �غ��� �ð� �ʰ� �ذ�
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

	// ���ȣ�� �Ҷ����� �� �� �ִ� �����ȣ�� ����
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