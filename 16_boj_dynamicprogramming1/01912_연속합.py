import sys
read = lambda : sys.stdin.readline().strip()

N = (int)(read())

S = [(int)(i) for i in read().split()]

def seqSum(start, A):

    N = len(A)
    ret = cnt = A[start]
    for i in range(start+1, N):
        # (지금까지의 합 + 다음원소) 보다
        # 다음 원소 달랑 하나가 더 크면
        if cnt + A[i] < A[i]:
            cnt = A[i]
        # 그렇지 않다면 계속 더해본다
        # 줄어들 수도 있지만 최대값을 저장해두어서 괜찮다
        else:
            cnt += A[i]

        # 지금까지의 연속합 중에 가장 큰 값을 계속 갱신한다
        # 이 부분은 가장 마지막에 해주어야 한다
        ret = max(ret, cnt)
    
    return ret


print("{}".format(seqSum(0,S)))