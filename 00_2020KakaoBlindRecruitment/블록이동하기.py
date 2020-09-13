# 최단 시간이므로 bfs 사용
import queue

global cache
global board
cache = set()

# 맵을 벗어나거나, 벽인지 확인
def check(rc):
    r, c, N = rc[0], rc[1], len(board)
    if r<0 or r>=N or c<0 or c>=N:
        return False
    if board[r][c] == 1:
        return False
    return True

# rc에 상대적인 곳에 있는 좌표를 반환
def toRC(rc, diff_s):
    r , c = rc[0], rc[1]
    if 'R' in diff_s:
        c += 1
    if 'L' in diff_s:
        c -= 1
    if 'U' in diff_s:
        r -= 1
    if 'D' in diff_s:
        r += 1
    return (r, c)

def turn_r(rc, diff):
    if diff == 'R':
        if check(toRC(rc,'D')) and check(toRC(rc,'RD')):
            return (rc, 'D')
    if diff == 'L':
        if check(toRC(rc,'U')) and check(toRC(rc,'LU')):
            return (toRC(rc,'U'), 'D')
    if diff == 'U':
        if check(toRC(rc,'R')) and check(toRC(rc, 'UR')):
            return (rc, 'R')
    if diff == 'D':
        if check(toRC(rc,'L')) and check(toRC(rc,'DL')):
            return (toRC(rc,'L'),'R')
    return None

def turn_l(rc, diff):
    if diff == 'R':
        if check(toRC(rc, 'U')) and check(toRC(rc,'RU')):
            return (toRC(rc,'U'), 'D')
    if diff == 'L':
        if check(toRC(rc,'D')) and check(toRC(rc,'LD')):
            return (rc, 'D')
    if diff == 'U':
        if check(toRC(rc, 'L')) and check(toRC(rc,'UL')):
            return (toRC(rc,'L'), 'R')
    if diff == 'D':
        if check(toRC(rc,'R')) and check(toRC(rc,'DR')):
            return (rc, 'R')
    return None


def move(rc1, diff):
    ret = set()
    rc2 = toRC(rc1, diff)
    # 4방향 이동
    if check(toRC(rc1,'R')) and check(toRC(rc2, 'R')):
        ret.add((toRC(rc1,'R'), diff))
    if check(toRC(rc1,'L')) and check(toRC(rc2, 'L')):
        ret.add((toRC(rc1,'L'), diff))
    if check(toRC(rc1,'U')) and check(toRC(rc2, 'U')):
        ret.add((toRC(rc1,'U'), diff))
    if check(toRC(rc1,'D')) and check(toRC(rc2, 'D')):
        ret.add((toRC(rc1,'D'), diff))
        
    # rc1 축, 90, -90 회전
    if turn_r(rc1, diff) != None:
        ret.add(turn_r(rc1, diff))
    if turn_l(rc1, diff) != None:
        ret.add(turn_l(rc1, diff))
    
    if diff == 'R':
        diff = 'L'
    elif diff == 'D':
        diff = 'U'
    else:
        print('ERROR')
    # rc2 축, 90, -90 회전
    if turn_r(rc2, diff)!=None:
        ret.add(turn_r(rc2, diff))
    if turn_l(rc2,diff) !=None:
        ret.add(turn_l(rc2, diff))

    real_ret = set()
    for r in ret:
        if not r in cache:
            real_ret.add(r)
    return real_ret

def solution(b):
    global board
    board = b
    answer = 0
    N = len(board)
    # 왼쪽 좌표가 항상, 위쪽 또는 왼쪽이라고 하자
    start = ((0, 0),'R', 0)  # 위치, 위치, 시간, rc1, rc2, t
    q = queue.Queue()
    q.put(start)    # 시작 위치 방문

    cache.add(((0,0), 'R')) # 방문 기록

    while not q.empty():
        rc1, diff, t = q.get()  # 확인할 위치
        rc2 = toRC(rc1, diff)   # 짝 좌표 확인
        if (rc1[0] == N-1 and rc1[1] == N-1)\
            or (rc2[0] == N-1 and rc2[1] == N-1):
            answer = t
            break

        can_go = move(rc1, diff) # 인접한 갈 수 있는 곳 확인
        for rc1, diff in can_go:
            q.put((rc1, diff, t+1))
            cache.add((rc1, diff))

    return t

solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]])


