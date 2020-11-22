def solution(n):
    answer = 0

    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            answer += div
            if (n // div) != div:
                answer += (n // div)

    return answer