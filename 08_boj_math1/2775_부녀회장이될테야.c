// 2017.10.9

#include <stdio.h>

int main() {
    int t, k, n, i, ka, na;
    int a[15][15] = { 0 };

    for (i = 0; i < 15; i++) {
        a[0][i] = i;
    }

    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d%d", &ka, &na);
        for (k = 1; k <= ka; k++) {
            for (n = 1; n <= na; n++) {
                a[k][n] = a[k - 1][n] + a[k][n - 1];
            }
        }
        printf("%d\n", a[ka][na]);
    }

    return 0;
}
