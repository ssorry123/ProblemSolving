#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

#define MAX 1000000
int N, M;
int arr[MAX + 1] = { 0, };	// 문제에 초기 [0, n]까지 N+1개의 원소가 있다고 함
bool ran = true;

int found(int i) {
	// 집합의 대표 idx(루트)를 찾았다면
	if (arr[i] == i) {
		return i;
	}
	// 최적화 :: 경로 압축 최적화
	return arr[i] = found(arr[i]);
}

// union 예약어 사용 불가능
void merge(int a, int b) {
	int a_root = found(a);
	int b_root = found(b);
	if ((a == b) || (a_root == b_root)) {	// 같은 그룹일 경우
		return;
	}

	// 야매 최적화 :: merge가 계속되는 경우 한쪽 쏠림 방지
	if (ran)
		arr[a_root] = b_root;
	else
		arr[b_root] = a_root;
	ran = !ran;

	return;
}

int main(int argc, char** argv) {

	cin >> N >> M;

	for (int i = 0; i <= N; ++i) {
		arr[i] = i;	// 초기 상태
	}


	for (int i = 0; i < M; ++i) {
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);	// cin -> scanf 변경 후 시간초과 해결;;
		// union
		if (a == 0) {
			merge(b, c);
		}// found
		else if (a == 1) {
			if ((b == c) || (found(b) == found(c))) {
				printf("YES\n");
			}
			else {
				printf("NO\n");
			}
		}// 이런 입력은 없음
		else {
			cout << "ERROR" << endl;
		}
	}

	return 0;
}