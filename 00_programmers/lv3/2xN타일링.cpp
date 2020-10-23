#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n) {
    int answer = 0;

    vector<int> dp(n + 1, 0);

    dp[1] = 1;  // n이 1일때 1개 가능
    dp[2] = 2;  // n이 2일때 2개 가능
    // dp[n] = dp[n-1] + dp[n-2]
    // 1칸 적은거에서 세로 하나 더하기
    // 2칸 적은거에서 정사각형 하나 더하기

    for (int i = 3; i <= n; ++i) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007;
    }

    return dp[n];
}