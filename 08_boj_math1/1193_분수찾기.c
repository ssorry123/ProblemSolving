// 2017.10.9

#include <stdio.h>

int main(void) {
    int i, m;
    scanf("%d", &m);

    for (i = 1; i > 0; i++) {
        m = m - i;
        if (m == 0) {
            if (i % 2 == 0) {
                printf("%d/1", i);
                break;
            }
            if (i % 2 == 1) {
                printf("1/%d", i);
                break;
            }
        }
        if (m < 0) {
            m = m + i; i--; m = m + i;
            if ((i + 2) % 2 == 1) {
                printf("%d/%d", m - i, -m + 2 * i + 2);
                break;
            }
            if ((i + 2) % 2 == 0) {
                printf("%d/%d", -m + 2 * i + 2, m - i);
                break;
            }
        }
    }
    return 0;
}
