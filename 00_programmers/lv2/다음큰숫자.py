def cnt_1bit(n):
    ret = 0

    mask = 1
    if n & mask != 0:
        ret += 1

    # 64bit int라 가정
    for i in range(63):
        mask <<= 1
        if n & mask != 0:
            ret += 1

    return ret

def solution(n):
    answer = 0

    MAX = 1000000
    n_cnt = cnt_1bit(n)
    for i in range(n+1, MAX+1):
        if n_cnt == cnt_1bit(i):
            return i

    return -1


for i in range(100):
    print(i, cnt_1bit(i))