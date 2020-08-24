#include <iostream>
#include <cmath>
using namespace std;

#define MAX 500
int N, K;
double doll[MAX];
double sum[MAX+1]; // [0, i)
// double sum_square[MAX+1];
double ret = (float)(1000000000000);

//K개 이상의 연속된 인형들의 표준편차를 구한다
//K개의 표준편차들, K + 1개의 표준편차들, ..., N개의 표준편차들
//위의 표준편차들 중 가장 작은 값을 선택한다

int main(int argc, char** argv) {
	cin >> N >> K;
	for (int i = 1; i <= N; ++i) {
		cin >> doll[i - 1];
		sum[i] = sum[i - 1] + doll[i - 1];
		// sum_square[i] = sum_square[i - 1] + doll[i - 1] * doll[i - 1];
	}

	int start = 0;
	while (K <= N) {
		double kk = (float)(K);
		// start부터 연속된 K개의 원소가 존재하면
		if (start + K <= N) {
			// 분산 구하기
			double m = (sum[start + K] - sum[start]) / kk;
			double variance = 0.0;
			for (int i = start; i < start + K; ++i) {
				double tmp = doll[i] - m;
				variance += tmp * tmp;
			}variance /= kk;

			/*
			for 문을 돌리지 않고 구하는 경우, 51%에서 오답
			sum_square에 값이 저장될때 너무 커지는건 아닐까 추정..
			*/
			//variance = variance + sum_square[start + K] - sum_square[start];
			//variance = variance + (kk * m * m);
			//variance = variance - 2 * m * (sum[start + K] - sum[start]);
			//variance /= kk;

			// 지금까지 구한 분산 중 가장 작은 값을 출력
			if (variance < ret) {
				ret = variance;
			}
			++start;
		}
		// start부터 연속된 K개의 원소가 존재하지 않으면
		else {
			++K;		// ㅏ증가
			start = 0;	// 0부터 다시 시작
		}
	}
	
	// 소수점 몇자리까지 출력할지 설정해주어야함
	cout.precision(12);
	// 분산을 표준편차로 바꾸고 출력
	cout << sqrt(ret);

	return 0;
}