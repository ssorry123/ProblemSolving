// 2017.10.10

#include <stdio.h>

int main() {
    int n, i = 1;

    scanf("%d", &n);
    if (n == 1) {
        printf("1");
    }

    if (n > 1) {
        while (1) {
            if (n > (3 * i * (i - 1) + 1) && n <= 3 * i * (i + 1) + 1) {
                printf("%d", i + 1);
                break;
            }
            i++;
        }
    }

    return 0;
}