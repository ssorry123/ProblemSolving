import math

# java로 똑같이 짰는데 효율성 테스트 통과못하는 매직
# python으로 하니까 됐다...
# 코테는 파이썬이 값,,

def solution(n, k):
    answer = []

    # 0번째 1, 1번째 2, ,,, 
    intList = []
    for i in range(1, n+1):
        intList.append(i)

    # k를 0부터 시작하도록
    k -= 1

    # n번째 숫자는 맨 왼쪽
    # 1번째 숫자는 맨 오른쪽
    while n>0:
        tmp = math.factorial(n-1)   # 가지수
        block = k // tmp            # 현재 자리에 들어갈 순서
        k = k % tmp                 # 다음 자리 위치에 넘겨줄 순서

        answer.append(intList.pop(block))
        n-=1

    return answer

