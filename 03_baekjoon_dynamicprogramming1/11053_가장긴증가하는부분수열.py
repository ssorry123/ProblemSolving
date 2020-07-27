import sys

read = lambda : sys.stdin.readline().strip()

N = (int)(read())

A = [(int)(i) for i in read().split()]

cache = [-1]*1001

def LIS(start, S):
    """
    LIS(int start, List S)
    """  
    n = len(S)

    if cache[start] != -1:
        return cache[start]


    ret = 1 # 자기 자신의 길이
    for i in range(start+1, n):
        # 시작 보다 큰 숫자를 발견하면
        if S[start] < S[i]:
            # 자기 자신의 길이 1을 더하는 것이 핵심 포인트
            candidate = 1 + LIS(i, S)
            ret = max(ret, candidate)
    
    cache[start] = ret
    return ret

max_length = 0
for i in range(N):
    max_length = max(max_length, LIS(i, A))
print(max_length)