// writed 2019

#include <stdio.h>
int cache[50];
int fibo(int n);
int main() {
	int i,tC,N;
	scanf("%d", &tC);

	for (i = 0; i < tC;i++) {
		int n;
		scanf("%d", &n);
		if (n == 0)
			printf("1 0\n");
		else {
			fibo(n);
			printf("%d %d\n", fibo(n - 1), fibo(n));
		}
	}
	return 0;
}
int fibo(int n) {
	if (cache[n] != 0)
		return cache[n];
	if (n == 0)
		return 0;
	if (n == 1) 
		return 1;
	cache[n] = fibo(n - 1) + fibo(n - 2);
	return cache[n];
}