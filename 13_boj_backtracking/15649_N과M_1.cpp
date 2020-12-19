#include<iostream>
#include<vector>

using namespace std;

#define MAX 8

int N, M;
int v[MAX] = {0,};
bool visited[MAX + 1] = {false,};
void dfs(int idx);		// idx == 삽입할 배열 index, 아래 cnt와 거의 같음
void print_v(int cnt);	// cnt == 배열 v의 크기, idx와 같지만 의미 구별

int main() {
	cin >> N >> M;
	
	dfs(0);

	return 0;
}
void dfs(int idx) {
	// 기저사례, N길이의 수열을 만든 경우
	if (idx == M) {
		print_v(idx);
		return;
	}

	for (int i = 1; i <= N; ++i) {
		// 선택하지 않은 수라면
		if (visited[i] == false) {
			v[idx] = i;			// idx 위치에 삽입
			visited[i] = true;	// 선택된 원소는 다시 선택 불가능
			dfs(idx + 1);
			visited[i] = false; // 출력된 후에는 다시 선택 가능
		}
	}
}

void print_v(int cnt) {
	for (int i = 0; i < cnt; ++i){
		cout << v[i] << ' ';
	}
	cout << "\n";
}