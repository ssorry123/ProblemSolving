def solution(n):
    ans = 0
    
    while n!=0:
        # 홀수면, 1 감소시켜 짝수로 만든다
        if n%2 == 1:
            ans += 1
            n -= 1
        # 짝수면, 순간이동 한다
        else:
            n = n//2

    print(ans)

    return ans