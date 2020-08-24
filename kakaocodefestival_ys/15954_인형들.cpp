#include <iostream>
#include <cmath>
using namespace std;

#define MAX 500
int N, K;
double doll[MAX];
double sum[MAX+1]; // [0, i)
// double sum_square[MAX+1];
double ret = (float)(1000000000000);

//K�� �̻��� ���ӵ� �������� ǥ�������� ���Ѵ�
//K���� ǥ��������, K + 1���� ǥ��������, ..., N���� ǥ��������
//���� ǥ�������� �� ���� ���� ���� �����Ѵ�

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
		// start���� ���ӵ� K���� ���Ұ� �����ϸ�
		if (start + K <= N) {
			// �л� ���ϱ�
			double m = (sum[start + K] - sum[start]) / kk;
			double variance = 0.0;
			for (int i = start; i < start + K; ++i) {
				double tmp = doll[i] - m;
				variance += tmp * tmp;
			}variance /= kk;

			/*
			for ���� ������ �ʰ� ���ϴ� ���, 51%���� ����
			sum_square�� ���� ����ɶ� �ʹ� Ŀ���°� �ƴұ� ����..
			*/
			//variance = variance + sum_square[start + K] - sum_square[start];
			//variance = variance + (kk * m * m);
			//variance = variance - 2 * m * (sum[start + K] - sum[start]);
			//variance /= kk;

			// ���ݱ��� ���� �л� �� ���� ���� ���� ���
			if (variance < ret) {
				ret = variance;
			}
			++start;
		}
		// start���� ���ӵ� K���� ���Ұ� �������� ������
		else {
			++K;		// ������
			start = 0;	// 0���� �ٽ� ����
		}
	}
	
	// �Ҽ��� ���ڸ����� ������� �������־����
	cout.precision(12);
	// �л��� ǥ�������� �ٲٰ� ���
	cout << sqrt(ret);

	return 0;
}