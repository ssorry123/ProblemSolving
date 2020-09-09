def turn_right(key):
    ''' 90도 회전 '''
    m = len(key)
    # 각 i번째 row들이 m-i번째 col이 된다
    ret = list()
    for _ in range(m):
        ret.append([0]*m)
    
    for r in range(m):
        for c in range(m):
            ret[c][m-r-1] = key[r][c]
    
    return ret

# 한 키를 lock에 맞춰보고 lock이 모두 꽉찼는지 확인
def match(vr, vc, lock_blank_cnt, key, lock):
    m = len(key)
    n = len(lock)

    for r in range(vr, vr+m):
        for c in range(vc, vc+m):
            if r>=0 and c>=0 and r<n and c<n:
                # 키의 돌기가 lock의 홈을 채우는 경우
                if lock[r][c] == 0 and key[r-vr][c-vc] == 1:
                    lock_blank_cnt -= 1
                # 돌기끼리 만나거나, 홈끼리 만나는 경우
                elif lock[r][c] == key[r-vr][c-vc]:
                    return False
                # 키의 홈과, lock의 돌기가 만나는 경우
                else:
                    continue

    # lock의 홈을 키의 돌기로 다 채웠다면
    if lock_blank_cnt == 0:
        return True
    else:
        return False


def solution(key, lock):
    # 각 정사각형 변의 길이 m, n
    m = len(key)
    n = len(lock)

    # lock을 채워야 하는 구멍의 수
    lock_blank_cnt = 0
    for row in lock:
        lock_blank_cnt += row.count(0)

    # 각 키를 회전시킨 배열 저장
    key_lotation = [key]
    for _ in range(3):
        key_lotation.append(turn_right(key_lotation[-1]))

    # 각 정사각형의 왼쪽위를 시작 지점이라 정하고,
    # lock 시작지점 rc(0,0)을 원점으로 할때,
    # key가 위치할 수 있는 가상의 좌표 rc(-(m-1), -(m-1)) ~ rc(n-1, n-1)
    # ex)3*3, 3*3의 경우 key는 (-2,-2)~(2,2)에 위치할 수 있다

    # 4가지 종류의 키에 대하여
    for k in key_lotation:
        # key가 위치하였을때 맞을 가능성이있는 r, c
        for r in range(-(m-1), n):
            for c in range(-(m-1), n):
                # 하나라도 맞는 방법이 있으면
                if match(r, c, lock_blank_cnt, k, lock):
                    return True

    return False