# 간단한 dp 문제

def solution(n):
    dp = [0] * 3
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp.append((dp[i-1] + dp[i-2])%1234567)
    
    return dp[n]