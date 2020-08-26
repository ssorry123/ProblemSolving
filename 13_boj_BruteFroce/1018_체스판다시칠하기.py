import sys
read = lambda : sys.stdin.readline().strip()

tmp = read().split()
# N*M 체스판
N = (int)(tmp[0])
M = (int)(tmp[1])

chess = list()
for _ in range(N):
    chess.append(read())

# 비용의 최대값
ret = 32
def check(r, c):
    global ret

    cnt = 0
    # B로 시작하는 체스판을 만들기위해 색을 바꿔야할때 최대 변경 회수->64
    here = 'B'
    # O(64) -> O(1)
    for row in range(r, r+8):
        for col in range(c, c+8):
            # 색을 바꿔야 하면
            if chess[row][col] != here:
                cnt += 1
            # 다음 체스판 색깔 변경
            if here == 'B':
                here = 'W'
            else:
                here = 'B'
        # row가 바뀌면
        if here == 'B':
            here = 'W'
        else:
            here = 'B'

    # B로 시작하는 체스판보다 W로 시작하는 체스판을 만드는게 더 비용이 적으면
    if cnt > 32:
        cnt = 64 - cnt
    ret = min(ret, cnt)
    return

# 선택 가능한 체스판 모두 검사, O(N^2)
for r in range(N-7):
    for c in range(M-7):
        check(r, c)
    
print(ret)