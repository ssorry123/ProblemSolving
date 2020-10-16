''' 대회 당시 AC ''' 
# 간단한 압축 문제

ret = [0 , 0]
def div(arr, r, c, size):
    global ret
    if size == 1:
        ret[arr[r][c]] += 1
        return
    
    check = arr[r][c]
    rediv = False
    # 범위 검사
    for i in range(r, r+size):
        for j in range(c, c+size):
            # 하나라도 다른게 있다면
            if arr[i][j] != check:
                rediv = True
                break
        if rediv==True:
            break
    
    # 모두 같다면 압축,
    if not rediv:
        ret[arr[r][c]] += 1
        return
    
    # 모두 같지 않다면, 분할해서 다시 해봄
    half = int(size/2)
    div(arr, r, c, half)
    div(arr, r + half, c, half)
    div(arr, r, c + half, half)
    div(arr, r + half, c + half, half)
    return


def solution(arr):
    answer = []

    # 카운터 초기화
    global ret
    ret = [0,0]

    div(arr, 0, 0, len(arr))

    answer = ret
    return answer