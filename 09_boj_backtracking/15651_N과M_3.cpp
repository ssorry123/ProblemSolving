#include<iostream>
#include<vector>

using namespace std;

#define MAX 7

int N, M;
int v[MAX] = { 0, };
void dfs(int idx);		// idx == ������ �迭 index, �Ʒ� cnt�� ���� ����
void print_v();

int main() {
	cin >> N >> M;

	dfs(0);

	return 0;
}
void dfs(int idx) {
	// �������, N������ ������ ���� ���
	if (idx == M) {
		print_v();
		return;
	}

	for (int i = 1; i <= N; ++i) {
		v[idx] = i;			// idx ��ġ�� ����
		dfs(idx + 1);
	}
}

void print_v() {
	for (int i = 0; i < M; ++i) {
		cout << v[i] << ' ';
	}
	cout << "\n";
}