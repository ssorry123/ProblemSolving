// 2018.09.23
#include <stdio.h>
#include <math.h>
int stack[10000], index = -1;
int result[10000], r_index = 0;

void input(char mes[]);
int main() {
	int n, i;
	scanf("%d\n", &n);
	for (i = 0; i < n; i++) {
		char mes[100];
		
		gets(mes);
		input(mes);
	}
	{
		int k;
		for (k = 0; k < r_index; k++)
			printf("%d\n",result[k]);
	}
	return 0;
}
void input(char mes[]) {
	if (strcmp(mes, "top") == 0) {
		if (index == -1)
			result[r_index++] = -1;
		else
			result[r_index++] = stack[index];
	}
	else if (strcmp(mes, "empty")==0) {
		if (index == -1)
			result[r_index++] = 1;
		else
			result[r_index++] = 0;
	}
	else if (strcmp(mes, "size")==0) {
		result[r_index++] = index + 1;
	}
	else if (strcmp(mes, "pop")==0) {
		if (index == -1)
			result[r_index++] = -1;
		else {
			result[r_index++] = stack[index--];
		}
	}
	else {
		int i,k = strlen(mes);
		int value=0,degree=0;
		for (i = k - 1; i >= 5;i--) {
			value = value + (mes[i] - 48)*(int)pow(10,degree++);
		}
		//printf("%d\n",value);
		stack[++index] = value;
	}
	return;
}