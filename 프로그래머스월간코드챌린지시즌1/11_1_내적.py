''' 대회 당시 AC '''

# 내적 구하기
def solution(a, b):
    answer = 0

    n = len(a)

    for i in range(n):
        answer += a[i]*b[i]

    return answer