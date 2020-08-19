#include<iostream>
#include<climits>	// INT_MAX
#include<cstdlib>	// abs
#include<algorithm>	// min, max

using namespace std;

#define NMAX 20
int MIN = INT_MAX;

int N;
int Ndiv2;
int S[NMAX][NMAX];
bool visited[NMAX];
int team[NMAX];

// cnt = �迭�� �� ��ġ, ���ݱ��� § ���� ��;
// me, ���ȣ��� �����̹Ƿ� �ߺ� ����
void dfs(int cnt, int me);
void check_diff();

int main(int argc, char** argv) {

	cin >> N;
	Ndiv2 = (int)(N / 2);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> S[i][j];
		}
	}
	//for (int i = 0; i < N; ++i) {
	//	for (int j = 0; j < N; ++j) {
	//		cout << S[i][j] << ' ';
	//	}cout << "\n";
	//}

	dfs(0, -1);
	cout << MIN;

	return 0;
}

void dfs(int cnt, int me) {
	if (cnt == Ndiv2) {
		check_diff();
		return;
	}

	for (int i = me + 1; i < N; ++i) {
		if (visited[i] == false) {
			team[cnt] = i;
			visited[i] = true;
			dfs(cnt + 1, i);
			visited[i] = false;
		}
	}
}

void check_diff() {
	// �ٸ� �� ���� �Է�
	for (int i = 0, j = Ndiv2; i < N; ++i) {
		if (visited[i] == false) {
			team[j++] = i;
		}
	}

	int scoreF = 0;
	int scoreB = 0;
	for (int i = 0; i < Ndiv2; ++i) {
		for (int j = 0; j < Ndiv2; ++j) {
			if (i != j) {
				scoreF += S[team[i]][team[j]];
				scoreB += S[team[i + Ndiv2]][team[j+Ndiv2]];
			}
		}
	}

	// �ּҰ� ����
	MIN = min(MIN, abs(scoreF-scoreB));
}