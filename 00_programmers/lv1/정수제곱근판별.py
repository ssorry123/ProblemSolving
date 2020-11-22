import math

def solution(n):
    answer = 0

    x = n ** 0.5
    x_floor = math.floor(x)

    # 차이가 저 정도 나면 같다고 판별
    if abs(x - x_floor) < 0.000001:
        return (x_floor + 1) ** 2
    return -1

