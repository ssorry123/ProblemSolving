def solution(n,a,b):
    answer = 1

    # 앞에 숫자를 작은 걸로
    if a > b:
        tmp = a
        a = b
        b = tmp

    
    while True:
        # a와 b가 붙게 된다면
        if a%2==1 and a+1 == b:
            break

        if a%2 == 1:
            a += 1
        if b%2 == 1:
            b += 1
        
        # 다음 라운드에서 번호
        a = a//2
        b = b//2
        answer += 1

    print(answer)

    return answer