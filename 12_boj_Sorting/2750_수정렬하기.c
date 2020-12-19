//2017.10.09
int main(void) {
	int n, i, j, z;
	int a[1000];
	scanf("%d", &n);
	for (i = 0; i < n; i++)
		scanf("%d", &a[i]);

	for (i = 0; i < n - 1; i++)
		for (j = i; j < n; j++)
			if (a[j] < a[i]) {
				z = a[i];
				a[i] = a[j];
				a[j] = z;
			}


	for (i = 0; i < n; i++)
		printf("%d\n", a[i]);
	return 0;

}