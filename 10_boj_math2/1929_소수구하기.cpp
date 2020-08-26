#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;
#define MAX 1000000

// n�� �Ҽ����� �ƴ��� �Ǻ��ϴ� �Լ�
bool isPrime(int n);

//(�����佺ü�׽��� ü�� ��ģ ��)
// false->�Ҽ�
// true-> �Ҽ��� �ƴ϶�� ���� Ȯ�ε�
bool num[MAX + 1] = { false, };
// �����佺�׳׽��� ü
void eratosPrime(int n) {
	// 1�� �Ҽ��� �ƴϴ�
	num[1] = true; num[2] = false;

	// sqrtn������ ����鸸 ������ ����ϴ�
	int sqrtn = sqrt(n);
	for (int i = 2; i <= sqrtn; ++i) {
		// �̹� �ɷ� ���ٸ�(�Ҽ��� �ƴ϶��)
		if (num[i] == true)
			continue;
		// i�� �Ҽ���� i�� ������� �Ҽ��� �ƴϴ�
		else if (isPrime(i)) {
			// j�� [2,i)�� ���� �տ��� �̹� ������(����ȭ)
			for (int j = i; i * j <= n; ++j)
				num[i * j] = true;
		}
	}

}
int main(int argc, char** argv) {
	int M, N;
	cin >> M >> N;
	eratosPrime(N);
	for (int i = M; i <= N; ++i) {
		if (!num[i])
			printf("%d\n", i);
	}

	return 0;
}

bool isPrime(int n) {
	// 2�� �Ҽ�
	if (n <= 2)
		return true;

	// i�� �����ٱ����� �˻�
	int sqrtn = sqrt(n);
	for (int i = 2; i <= sqrtn; ++i)
		if (n % i == 0)
			return false;
	return true;
}