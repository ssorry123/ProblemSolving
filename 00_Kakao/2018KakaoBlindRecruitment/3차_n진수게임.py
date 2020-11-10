# 진수 변환기
def convertN(N, val):
    ret = ''
    
    if val == 0:
        return '0'

    arr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while val != 0:
        ret = arr[val%N] + ret
        val = val // N

    return ret

# n진수, 나의 t개 미리 구함, m명, 나의 순서(1~)
def solution(n, t, m, p):
    answer = ''

    # m명이 말해야 하는 숫자들을 여유롭게 구한다
    tell = ''
    for i in range(0, t*m):
        tell += convertN(n, i)


    cnt = 0
    p -= 1
    for i in range(len(tell)):
        # 내가 말해야 하는 순서라면, 미리 구해놓자
        if i%m == p:
            answer += tell[i]
            cnt += 1
            if cnt == t:
                break


    return answer

