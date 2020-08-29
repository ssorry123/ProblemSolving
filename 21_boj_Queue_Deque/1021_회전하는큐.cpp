#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

// 큐의 크기
int N;
// 큐에서 빼야하는 것이 있는 위치
vector<int> v;
void left_shift() {
	for (int i = 0; i < v.size(); ++i)
		if (--v[i] < 0)
			v[i] = N - 1;
}
void right_shift() {
	for (int i = 0; i < v.size(); ++i)
		if (++v[i] >= N)
			v[i] = 0;
}
void pop_left() {
	// 큐 개수 감소
	v.erase(v.begin());
	--N;
	// 빼야 하는 것이 존재하는 위치 땡기기
	left_shift();
}

int main(int argc, char** argv) {
	int M;	// N 큐의 크기, M 뽑아내려고 하는 수의 개수
	cin >> N >> M;
	int tmp;
	for (int i = 0; i < M; ++i) {
		scanf("%d", &tmp);
		v.push_back(tmp - 1);
	}
	int ret = 0;
	while (!v.empty()) {
		int toGet = v[0];
		// 빼야할 것이 뺄 수 있는 곳에 있다면
		if (toGet == 0) {
			pop_left();
		}
		// 빼야할 것이 뺄 수 없는 곳에 있다면
		else {
			// 왼쪽으로 돌리는게 더 적게 든다면
			if (toGet <= N - toGet) {
				for (int i = 0; i < toGet; ++i) {
					left_shift(); ++ret;
				}
			}
			// 오른쪽으로 돌리는게 더 적게 든다면
			else {
				for (int i = 0; i < N - toGet; ++i) {
					right_shift(); ++ret;
				}
			}
		}
	}

	cout << ret << endl;

	return 0;
}