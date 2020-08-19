#include<iostream>

using namespace std;

#define MAX 15


// �������� ��� 0���� �ʱ�ȭ(ǥ��)(���� ����..?)
// !!���� ���� �� �ִ����� ǥ���ϴ� ���� �ƴ϶�, ���� �����ϴ� ���� ǥ��!!
bool chess[MAX][MAX];
int N;			// N*N ü����
int ret = 0;

void dfs(int r);
bool canQueen(int r, int c);
void print_chess();

int main() {
	// print_chess();
	cin >> N;

	dfs(0);

	cout << ret;

	return 0;
}
void dfs(int r) {
	if (r == N) {
		++ret;
		return;
	}

	for (int c = 0; c < N; c++) {
		// �ش� ��ġ�� ���� ���� �� �ִ� ���
		if (canQueen(r, c) == true) {
			chess[r][c] = true;		// �� ����
			dfs(r + 1);				// �� ���� ���·� ���� row �˻�
			chess[r][c] = false;	// �ش� ��ġ�κ��� �˻簡 �Ϸ�Ǹ� �� ����
		}
	}

}
bool canQueen(int r, int c) {
	bool ret_canQueen = true;

	// �ش� ���� ���� �ִ� ���
	for (int row = 0; row < N; ++row) {
		if (chess[row][c] == true) {
			ret_canQueen = false;
			break;
		}
	}
	if (ret_canQueen == false) {
		return ret_canQueen;
	}

	// ���� ����, ������ �밢���� ���� �ִ� ���
	int diff = 1;
	for (int row = r - 1; row >= 0; --row) {
		int col = c + diff;
		if ((col < N) && (chess[row][col] == true)) {
			ret_canQueen = false;
			break;
		}
		col = c - diff;
		if ((col >= 0) && (chess[row][col] == true)) {
			ret_canQueen = false;
			break;
		}
		++diff;
	}
	
	return ret_canQueen;
}

void print_chess() {
	for (int i = 0; i < MAX; ++i) {
		for (int j = 0; j < MAX; ++j) {
			cout << chess[i][j] << ' ';
		}
		cout << "\n";
	}
}