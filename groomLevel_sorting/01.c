#include <stdio.h>
#include <malloc.h>
int main() {
	int sizeA, sizeB, sizeRet;
	int i, j, k;
	int* a, * b, *ret;

	scanf_s("%d %d", &sizeA, &sizeB);

	a = (int*)malloc(sizeA * sizeof(int));
	b = (int*)malloc(sizeB * sizeof(int));
	sizeRet = sizeA + sizeB;
	ret = (int*)malloc(sizeRet * sizeof(sizeRet));

	for (i = 0; i < sizeA; i++) {
		scanf_s("%d", &a[i]);
	}

	for (i = 0; i < sizeB; i++) {
		scanf_s("%d", &b[i]);
	}

	//for (i = 0; i < sizea; i++) {
	//	printf("%d ", a[i]);
	//}printf("\n");

	//for (i = 0; i < sizeb; i++) {
	//	printf("%d ", b[i]);
	//}printf("\n");

	i = j = k = 0;
	while (1) {
		if (i < sizeA && j < sizeB) {
			if (a[i] < b[j])
				ret[k++] = a[i++];
			else
				ret[k++] = b[j++];
		}
		else if (i == sizeA && j < sizeB) {
			ret[k++] = b[j++];
		}
		else if (i < sizeA && j == sizeB) {
			ret[k++] = a[i++];
		}
		else {
			break;
		}
	}

	//if (k == sizeRet)
	//	printf("well");
	//else
	//	printf("suck");
	
	for(k = 0; k<sizeRet; k++){
		printf("%d ", ret[k]);
	}

	free(a);
	free(b);
	return 0;
}
