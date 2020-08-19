#include<iostream>
#include<vector>

using namespace std;

#define SIZE 9

int sudoku[SIZE][SIZE];
//int blank_r[SIZE * SIZE];
//int blank_c[SIZE * SIZE];
vector< pair<int, int> > blank;

bool find_one = false;
void dfs(int cnt);
void print_sudoku();
void candi_ints(int r, int c, bool *list);

int main(int argc, char** argv) {
	// 입력부분
	for (int i = 0; i < SIZE; ++i) {
		for (int j = 0; j < SIZE; ++j) {
			int tmp = 0;
			cin >> tmp;
			if (tmp == 0) {
				blank.push_back(make_pair(i, j));
			}
			sudoku[i][j] = tmp;
		}
	}

	// 함수 실행
	find_one = false;
	dfs(0);

	return 0;
}

void dfs(int cnt) {
	// cout << "cnt " << cnt << endl;

	// 빈칸을 모두 채웠다면
	if (cnt == blank.size()) {
		find_one = true;
		print_sudoku();
		return;
	}

	// 현재 빈칸의 위치 소환
	int r = blank[cnt].first;
	int c = blank[cnt].second;

	// 현재 빈칸에 사용할 수 있는 수 업데이트
	// 이 부분에 위치하면 매번 i가 가능한지 검사할 필요없다
	bool list[SIZE + 1] = { false, };
	candi_ints(r, c, list);

	for (int i = 1; i <= SIZE; ++i) {
		// 첫번째 정답을 발견했다면 그냥 종료
		if (find_one) {
			return;
		}
		 
		if (list[i]) {
			sudoku[r][c] = i;	// 쓴다
			dfs(cnt + 1);		// 다음 빈칸으로 이동한다
			sudoku[r][c] = 0;	// 쓴 것을 지운다
		}
	}

}
void candi_ints(int r, int c, bool* list) {
	int sectorRow = ((int)(r / 3)) * 3;
	int sectorCol = ((int)(c / 3)) * 3;
	// cout << sectorRow << " " << sectorCol << endl;

	// 가능한 수들의 배열 초기화
	// index 0 은 사용하지 않음
	for (int i = 1; i <= SIZE; ++i) {
		list[i] = true;
	}

	for (int i = 0; i < SIZE; ++i) {
		list[sudoku[r][i]] = false;	// row 검사
		list[sudoku[i][c]] = false;	// col 검사
	}

	// 3*3 검사
	for (int i = sectorRow; i < sectorRow + 3; ++i) {
		for (int j = sectorCol; j < sectorCol + 3; ++j) {
			list[sudoku[i][j]] = false;
		}
	}
}


void print_sudoku() {
	for (int i = 0; i < SIZE; ++i) {
		for (int j = 0; j < SIZE; ++j) {
			cout << sudoku[i][j] << " ";
		}cout << "\n";
	}
}