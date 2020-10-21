// 2017.11.6

#include <stdio.h>

int main() {
    int a, b, c, t, i;
    int A, B;

    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        A = 1;
        scanf("%d%d%d", &a, &b, &c);
        c--;
        B = c / a + 1;
        A = c % a + 1;
        printf("%d%02d\n", A, B);
    }
    return 0;
}
