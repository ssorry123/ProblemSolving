#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;
#define MAX 1000000

// n이 소수인지 아닌지 판별하는 함수
bool isPrime(int n);

//(에라토스체네스의 체를 거친 후)
// false->소수
// true-> 소수가 아니라는 것이 확인됨
bool num[MAX + 1] = { false, };
// 에라토스테네스의 체
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
int main(int argc, char** argv) {

	int k = 0;	// 1~k까지 소수를 판별함
	while (true) {
		int n;
		scanf("%d", &n);
		if (n == 0)
			break;

		int n2 = 2 * n;
		// 2N까지 소수를 판별하지 않았다면
		if (k < n2) {
			eratosPrime(n2);
			k = n2;
		}

		int cnt = 0;
		// (N,2N]의 소수개수 출력
		for (int i = n + 1; i <= n2; ++i) {
			if (!num[i])
				++cnt;
		}
		// printf("ans : %d\n", cnt);
		printf("%d\n", cnt);
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