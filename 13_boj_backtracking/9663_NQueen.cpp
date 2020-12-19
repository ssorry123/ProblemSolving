#include<iostream>

using namespace std;

#define MAX 15


// 전역변수 모두 0으로 초기화(표준)(보장 가능..?)
// !!퀸을 놓을 수 있는지를 표기하는 것이 아니라, 퀸이 존재하는 곳을 표시!!
bool chess[MAX][MAX];
int N;			// N*N 체스판
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
		// 해당 위치에 퀸을 놓을 수 있는 경우
		if (canQueen(r, c) == true) {
			chess[r][c] = true;		// 퀸 놓기
			dfs(r + 1);				// 퀸 놓은 상태로 다음 row 검사
			chess[r][c] = false;	// 해당 위치로부터 검사가 완료되면 퀸 빼기
		}
	}

}
bool canQueen(int r, int c) {
	bool ret_canQueen = true;

	// 해당 열에 퀸이 있는 경우
	for (int row = 0; row < N; ++row) {
		if (chess[row][c] == true) {
			ret_canQueen = false;
			break;
		}
	}
	if (ret_canQueen == false) {
		return ret_canQueen;
	}

	// 위로 왼쪽, 오른쪽 대각선에 퀸이 있는 경우
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