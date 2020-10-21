// 2017.7.30

#include <stdio.h>

int main() {
    int n, i;
    scanf("%d", &n);

    if (n % 5 == 0) {    //5
        printf("%d", n / 5);
        goto A;
    }
    else {    //5,3
        for (i = n / 5; i >= 1; i--) {
            if ((n - 5 * i) >= 3 && (n - 5 * i) % 3 == 0) {
                printf("%d", i + (n - 5 * i) / 3);
                goto A;
            }
        }
    }
    if (n % 3 == 0)    //3
        printf("%d", n / 3);
    else         //else
        printf("%d", -1);
A:
    return 0;
}