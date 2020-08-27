#include <iostream>
#include <cstdio>
#include <cmath>        // floor
#include <algorithm>    // sort

using namespace std;

#define MAX 500000

int N;
// MAX가 크므로 main내에서 지역변수가 아닌 전역변수로 할당
int arr[MAX] = { 0, };
// -4000~-1 [0, 3999], 0~4000 [4000, 8000]
int freq1[4001 + 4000] = { 0, };	// 정렬하여 최대 빈도 수 구함
int freq2[4001 + 4000] = { 0, };	// 복사본
int sum = 0;

int main(int argc, char** argv) {
	scanf("%d", &N);

	int tmp;
	for (int i = 0; i < N; ++i) {
		scanf("%d", &tmp);
		sum += tmp;
		arr[i] = tmp;
		// 최빈값 기록
		if (tmp >= 0) {
			++freq1[tmp + 4000];
			++freq2[tmp + 4000];
		}
		else {
			++freq1[tmp + 4000];
			++freq2[tmp + 4000];
		}
	}
	// 오름차순 정렬
	sort(arr, arr + N);

	// 최대 빈도 수 구하기
	sort(freq1, freq1 + 8001);
	int freq_max = freq1[8000];
	// 최빈값 인덱스 구하기
	int freq_idx = -1;
	int freq_cnt = 0;
	for (int i = 0; i < 8001; ++i) {
		if (freq2[i] == freq_max) {
			freq_idx = i;
			++freq_cnt;
		}
		if (freq_cnt == 2)
			break;
	}


	// cout << "answer" << endl;
	// 산술평균,, floor를 해줘야함
	// 오답 이유 -> (int)가 내림이라는 것이 보장되지 않는다
	cout << (int)floor((double)(sum) / N + 0.5) << endl;
	// 중앙값
	cout << arr[N / 2] << endl;
	// 최빈값
	cout << freq_idx - 4000 << endl;
	// 범위
	cout << arr[N - 1] - arr[0] << endl;

	return 0;
}