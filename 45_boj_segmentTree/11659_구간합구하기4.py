# 세그멘테이션트리 문제지만 부분합으로 해결

import sys
read = lambda : sys.stdin.readline().strip().split()

tmp = read()
N = (int)(tmp[0])  # 수의 개수
M = (int)(tmp[1])  # 합을 구해야 하는 개수

sum = [0] * (N+1)   # sum[i] == 1번부터 i번까지의 합
arr = read()        # arr[0]의 값 == 1번째 수

# O(N)
for i in range(1, N+1):
    arr[i-1] = (int)(arr[i-1])
    sum[i] = sum[i-1] + arr[i-1]


for _ in range(M):
    tmp = read()
    i = (int)(tmp[0])
    j = (int)(tmp[1])
    #print("answer {0}".format(sum[j] - sum[i-1]))
    # O(1)
    print(sum[j] - sum[i-1])