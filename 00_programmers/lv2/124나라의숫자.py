def solution(N):
    answer = ''

    # 0은 없다;
    # N = X0 * 3^0  +  X1 * 3^1  +  X2 * 3^2  +  ...  +  Xn * 3^n
    # X는 1, 2, 3 (10진수)중 하나다
    
    while N != 0:
        # X0이 3이다
        if N % 3 == 0:
            answer = '4' + answer
            N -= 3
        # X0이 1 or 2 다
        else:
            answer = str(int(N % 3)) + answer
            N -= (N % 3)
        N /= 3

    return answer


for i in range(50):
    print(i, solution(i))