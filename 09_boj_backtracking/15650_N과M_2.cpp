#include<iostream>

using namespace std;

#define MAX 8

int N, M;
bool visited[MAX + 1] = { false, };
int list[MAX + 1] = { 0, };

void dfs1(int idx);
void dfs2(int idx, int last);
void print_list();

int main() {
	cin >> N >> M;

	// dfs1(1);
	dfs2(1, 0);

	return 0;
}

void dfs1(int idx) {
	if (idx == M+1) {
		print_list();
		return;
	}

	for (int i = 1; i <= N; ++i) {
		if ((visited[i] == false) && (list[idx - 1] < i)) {
			visited[i] = true;
			list[idx] = i;
			dfs1(idx + 1);
			visited[i] = false;
		}
	}
}
void dfs2(int idx, int last) {
	if (idx == M + 1) {
		print_list();
		return;
	}

	for (int i = last + 1; i <= N; i++) {
		if (visited[i] == false) {
			visited[i] = true;
			list[idx] = i;
			dfs2(idx + 1, i);
			visited[i] = false;
		}
	}

}

void print_list() {
	for (int i = 1; i <= M; ++i) {
		cout << list[i] << " ";
	}
	cout << "\n";
}