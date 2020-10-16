// 파이썬으로 똑같이 짜면
// 99%~100%채점 단계에서 런타임 에러가난다
// 왠지 모르겠따

// DP인 것을 쉽게 떠올릴 수 있을까?

#include <stdio.h>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 3;

    for (int i = 3; i <= n; ++i)
        dp[i] = (dp[i - 1] % 10007 + (dp[i - 2] * 2) % 10007) % 10007;

    printf("%d\n", dp[n]);

    return 0;
}