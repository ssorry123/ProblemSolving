// AC, 슬프게도, 이 문제만 풀었다
#include <iostream>
#include <algorithm>
#include<cstdlib>
#include<vector>

using namespace std;

#define MAX 200000

int Answer;
int N, K;
int a[MAX];
int b[MAX];

int main(int argc, char** argv)
{
	int T, test_case;

	cin >> T;
	for (test_case = 0; test_case < T; test_case++)
	{

		// 입력부분 //
		// 메뉴 수 N 은 다이어트 기간 K보다 크거나 같다
		cin >> N >> K;
		for (int i = 0; i < N; ++i)
			cin >> a[i];
		for (int i = 0; i < N; ++i)
			cin >> b[i];

		 //칼로리 적은것만 먹기
		 sort(a, a + N);
		 sort(b, b + N);
         // 그리디
		 int ret = 0;
		 for (int i = 0; i < K; ++i) {
			ret = max(ret, a[i] + b[K - 1 - i]);
		 }
		 Answer = ret;

		cout << "Case #" << test_case + 1 << endl;
		cout << Answer << endl;
	}

	return 0;//Your program should return 0 on normal termination.
}