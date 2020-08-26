#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;
#define MAX 10000

bool isPrime(int n);
bool num[MAX + 1] = { false, };
void eratosPrime(int n);
int main(int argc, char** argv) {
	int T;
	scanf("%d", &T);
	// 10000까지 소수 판별하기
	eratosPrime(10000);

	for (int testCase = 0; testCase < T; ++testCase) {
		int n;
		scanf("%d", &n);
		vector<int> prime;
		for (int i = 2; i < n; ++i)
			if (!num[i])
				prime.push_back(i);

		int a = 0, b = 0, diff_ab = n;
		for (int i = 0; i < prime.size() && prime[i] <= (n/2); ++i) {
			for (int j = i; j < prime.size(); ++j) {
				if (prime[i] + prime[j] == n) {
					if (abs(prime[i] - prime[j]) < diff_ab) {
						a = prime[i];
						b = prime[j];
						diff_ab = abs(a - b);
					}
				}
			}
		}
		printf("%d %d\n", a, b);
	}

	return 0;
}

bool isPrime(int n) {
	// 2는 소수
	if (n <= 2)
		return true;

	// i의 제곱근까지만 검사
	int sqrtn = sqrt(n);
	for (int i = 2; i <= sqrtn; ++i)
		if (n % i == 0)
			return false;
	return true;
}
void eratosPrime(int n) {
	// 1은 소수가 아니다
	num[1] = true; num[2] = false;

	// sqrtn까지의 배수들만 지워도 충분하다
	int sqrtn = sqrt(n);
	for (int i = 2; i <= sqrtn; ++i) {
		// 이미 걸러 졌다면(소수가 아니라면)
		if (num[i] == true)
			continue;
		// i가 소수라면 i의 배수들은 소수가 아니다
		else if (isPrime(i)) {
			// j가 [2,i)인 경우는 앞에서 이미 지웠다(최적화)
			for (int j = i; i * j <= n; ++j)
				num[i * j] = true;
		}
	}

}