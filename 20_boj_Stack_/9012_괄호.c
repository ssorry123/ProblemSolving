//2018.09.23
#include <stdio.h>
#include <string.h>

int index = -1;
void answer(char arr[]);
int main() {
	int testCase,i;
	
	scanf("%d\n", &testCase);
	for (i = 0; i < testCase; i++) {
		char arr[101];
		gets(arr);
		answer(arr);
	}
	return 0;
}
void answer(char arr[]) {
	int i,size = strlen(arr);
	int true = 1;

	for (i = 0; i < size; i++) {
		if (arr[i] == '(') {
			index++;
		}
		else {
			if (index <= -1) {
				true = 0;
				break;
			}
			index--;
		}
	}
	if (index > -1)
		true = 0;
	if (true == 0)
		printf("NO\n");
	else
		printf("YES\n");
    index=-1;
}