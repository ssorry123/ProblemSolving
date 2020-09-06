# 한 줄씩 검사
def check1(num, n):
    ret_str = ''
    for i in range(n):
        c = 1 << i      # 오른쪽에서 i번째 비트 검사
        ret = num & c   # 결과는 0 또는 2^i
        # 오른쪽 칸(비트)부터 검사하므로 왼쪽(앞)에다가 붙여줘야 함
        if ret == 0:
            ret_str = ' ' + ret_str
        else:
            ret_str = '#' + ret_str
    return ret_str

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # or 연산 결과는 둘중 하나라도, 또는 둘다 1(벽)이면 -> 1
        # 둘다 0이었던 경우 -> 0
        ret = arr1[i] | arr2[i]
        answer.append(check1(ret, n))

    return answer


print (solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])