#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

#define MAX_PRIORITY 9

int main(int argc, char** argv) {
	int testCase;
	cin >> testCase;

	for (int t = 0; t < testCase; ++t) {
		// N 전체 문서의 개수, M 궁금한 문서의 큐에서 위치
		int N, M;
		scanf("%d %d", &N, &M);

		queue<int> q;
		int pq[MAX_PRIORITY + 1] = { 0, };
		int tmp;
		for (int i = 0; i < N; ++i) {
			scanf("%d", &tmp);
			q.push(tmp);
			++pq[tmp];
		}
		int cnt = 0;	// 출력 순서
		// 우선순위가 높은 것부터 출력
		for (int priority = 9; priority >= 1; --priority) {
			// 해당 우선순위에 출력할 문서가 남아있으면
			while (pq[priority] > 0) {
				// 출력할 문서중 가장 높은 우선순위이면
				if (q.front() == priority) {
					q.pop();
					--pq[priority];	// 해당 우선순위 문서 수 감소
					++cnt;	// 증가 후 cnt -> 현재 문서가 출력된 순서
					--M;	// 궁금한 문서의 위치가 땡겨짐
					// 출력한 문서가 궁금한 문서였다면
					if (M == -1) {
						printf("%d\n", cnt);
					}
				}
				// 가장 큰 우선순위가 아니라면
				else {
					q.push(q.front());	// 뒤로 옮김
					q.pop();			// 제거
					--M;	// 궁금한 문서의 위치 땡겨짐
					// 맨 뒤로 갔다면
					if (M == -1) {
						M = q.size() - 1;
					}
				}
			}
		}
	}

	return 0;
}