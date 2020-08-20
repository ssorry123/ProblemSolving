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
	// �Էºκ�
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

	// �Լ� ����
	find_one = false;
	dfs(0);

	return 0;
}

void dfs(int cnt) {
	// cout << "cnt " << cnt << endl;

	// ��ĭ�� ��� ä���ٸ�
	if (cnt == blank.size()) {
		find_one = true;
		print_sudoku();
		return;
	}

	// ���� ��ĭ�� ��ġ ��ȯ
	int r = blank[cnt].first;
	int c = blank[cnt].second;

	// ���� ��ĭ�� ����� �� �ִ� �� ������Ʈ
	// �� �κп� ��ġ�ϸ� �Ź� i�� �������� �˻��� �ʿ����
	bool list[SIZE + 1] = { false, };
	candi_ints(r, c, list);

	for (int i = 1; i <= SIZE; ++i) {
		// ù��° ������ �߰��ߴٸ� �׳� ����
		if (find_one) {
			return;
		}
		 
		if (list[i]) {
			sudoku[r][c] = i;	// ����
			dfs(cnt + 1);		// ���� ��ĭ���� �̵��Ѵ�
			sudoku[r][c] = 0;	// �� ���� �����
		}
	}

}
void candi_ints(int r, int c, bool* list) {
	int sectorRow = ((int)(r / 3)) * 3;
	int sectorCol = ((int)(c / 3)) * 3;
	// cout << sectorRow << " " << sectorCol << endl;

	// ������ ������ �迭 �ʱ�ȭ
	// index 0 �� ������� ����
	for (int i = 1; i <= SIZE; ++i) {
		list[i] = true;
	}

	for (int i = 0; i < SIZE; ++i) {
		list[sudoku[r][i]] = false;	// row �˻�
		list[sudoku[i][c]] = false;	// col �˻�
	}

	// 3*3 �˻�
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