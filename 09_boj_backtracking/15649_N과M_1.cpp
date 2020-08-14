#include<iostream>
#include<vector>

using namespace std;

#define MAX 8

int N, M;
int v[MAX] = {0,};
bool visited[MAX + 1] = {false,};
void dfs(int idx);		// idx == ������ �迭 index, �Ʒ� cnt�� ���� ����
void print_v(int cnt);	// cnt == �迭 v�� ũ��, idx�� ������ �ǹ� ����

int main() {
	cin >> N >> M;
	
	dfs(0);

	return 0;
}
void dfs(int idx) {
	// �������, N������ ������ ���� ���
	if (idx == M) {
		print_v(idx);
		return;
	}

	for (int i = 1; i <= N; ++i) {
		// �������� ���� �����
		if (visited[i] == false) {
			v[idx] = i;			// idx ��ġ�� ����
			visited[i] = true;	// ���õ� ���Ҵ� �ٽ� ���� �Ұ���
			dfs(idx + 1);
			visited[i] = false; // ��µ� �Ŀ��� �ٽ� ���� ����
		}
	}
}

void print_v(int cnt) {
	for (int i = 0; i < cnt; ++i){
		cout << v[i] << ' ';
	}
	cout << "\n";
}