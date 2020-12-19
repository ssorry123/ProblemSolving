#pragma warning(disable: 4996);
#include <stdio.h>

int main() {
	int a;
	scanf("%d", &a);
	if (a % 400 == 0) {
		printf("1");
		return 0;
	}
	if (a % 4 == 0 && a % 100 != 0) {
		printf("1");
		return 0;
	}
	
	printf("0");

	return 0;
}