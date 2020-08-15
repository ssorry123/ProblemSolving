#include<iostream>

using namespace std;

#define MAX 8

int N, M;
int list[MAX] = { 0, };

void dfs2(int idx, int last);
void print_list();

int main() {
	cin >> N >> M;

	dfs2(0, 1);

	return 0;
}

void dfs2(int idx, int last) {
	if (idx == M) {
		print_list();
		return;
	}

	for (int i = last; i <= N; i++) {
			list[idx] = i;
			dfs2(idx + 1, i);
	}
}

void print_list() {
	for (int i = 0; i < M; ++i) {
		cout << list[i] << " ";
	}
	cout << "\n";
}