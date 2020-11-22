# 1부터 n사이에 있는 소수 개수 찾기

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    for div in range(2, int(num**0.5) + 1):
        # 1과 자기 자신 외 숫자로 나눠지면
        if num % div == 0:
            return False
    return True
    

def solution(n):
    answer = 0

    # 초기 모두 소수로 판별
    eratos_p = [True] * (n+1)
    eratos_p[0] = eratos_p[1] = False   # 0과 1은 소수가 아니다

    for num in range(2, n+1):
        # 현재 수가 소수가 아님으로 판별되었으면
        if eratos_p[num] == False:
            continue

        # 현재 수가 일단 소수로 가정되었다면
        # 그런데 진짜 소수라면, 소수의 배수들은 소수가 아니다
        if is_prime(num):
            # num*2, num*3, ..., num*
            time = 2
            while num * time <= n:
                eratos_p[num * time] = False
                time += 1

    answer = eratos_p.count(True)

    return answer

