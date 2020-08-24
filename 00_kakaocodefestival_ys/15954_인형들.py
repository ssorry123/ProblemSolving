# python3 시간초과
# pypy3 통과

import math
import sys

tmp = input().split()
N = (int)(tmp[0])
K = (int)(tmp[1])

# K개 이상의 연속된 인형들의 표준편차를 구한다
# K개의 표준편차들, K+1개의 표준편차들,..., N개의 표준편차들
# 위의 표준편차들 중 가장 작은 값을 선택한다

#[0, i)
sum = [0] * (N + 1)
# sum_square = [0] * (N + 1)
doll = sys.stdin.readline().strip().split()
min_variance = (float)(10**12)

for i in range(1, N+1):
    doll[i-1] = (float)(doll[i-1])
    sum[i] = sum[i-1] + doll[i-1]
    # sum_square[i] = sum_square[i-1] + doll[i-1] * doll[i-1]

start = 0
k = K
while k<=N:
    # start부터 연속된 k개의 분산을 구할 수 있는 경우
    if start + k <= N:
        # doll[start] ~ doll[start + k - 1] 까지의 합 / k
        m = (sum[start + k] - sum[start]) / k
        # 분산 구하기
        variance = 0
        for i in range(start, start + k):
            tmp = doll[i] - m
            variance += tmp*tmp
        variance = variance / k

        if variance < min_variance:
            min_variance = variance

        start += 1

    # start부터 연속된 k개의 분산을 구할 수 없는 경우
    # k를 늘리고 start는 0부터 다시 시작
    else:
        k += 1
        start = 0

print(math.sqrt(min_variance))