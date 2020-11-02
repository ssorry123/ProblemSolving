def solution(A,B):
    answer = 0

    # 가장 큰값과 가장 작은 값을 곱한다
    A = sorted(A)
    B = sorted(B, reverse=True)

    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer