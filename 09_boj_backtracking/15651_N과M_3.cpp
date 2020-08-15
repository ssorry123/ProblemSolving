#include<iostream>
#include<vector>

using namespace std;

#define MAX 7

int N, M;
int v[MAX] = { 0, };
void dfs(int idx);		// idx == 삽입할 배열 index, 아래 cnt와 거의 같음
void print_v();

int main() {
	cin >> N >> M;

	dfs(0);

	return 0;
}
void dfs(int idx) {
	// 기저사례, N길이의 수열을 만든 경우
	if (idx == M) {
		print_v();
		return;
	}

	for (int i = 1; i <= N; ++i) {
		v[idx] = i;			// idx 위치에 삽입
		dfs(idx + 1);
	}
}

void print_v() {
	for (int i = 0; i < M; ++i) {
		cout << v[i] << ' ';
	}
	cout << "\n";
}