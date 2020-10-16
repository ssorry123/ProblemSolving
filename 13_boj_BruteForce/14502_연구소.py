'''
완전 탐색에 넣은 이유
맵의 크기가 작은 것을 알고, 완전탐색을 떠올리는 것이 핵심이었음
'''

import sys
read = lambda : sys.stdin.readline().strip()

# R,C는 최대 8로 작다, 완전 탐색
R, C = map(int, read().split())

arr = list()
for _ in range(R):
    arr.append(list(map(int, read().split())))

# 바이러스 위치 파악
virusRC = list()
for i in range(R):
    for j in range(C):
        if arr[i][j] == 2:
            virusRC.append((i,j))

def dfs(r, c, newarr):
    # 최초 newarr[r][c] == 2
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue

        if newarr[nr][nc]==0:
            newarr[nr][nc] = 2  # 바이러스 감염
            dfs(nr, nc, newarr)

# 벽을 3개 세우고
# dfs나 bfs로 바이러스가 퍼진 곳을 찾고, 안전구역 기록
answer = -1
for a in range(R*C):
    for b in range(a+1, R*C):
        for c in range(b+1, R*C):
            # 1차원 좌표 2차원 자표로
            ar, ac = a//C, a%C
            br, bc = b//C, b%C
            cr, cc = c//C, c%C
            if arr[ar][ac]==0 and arr[br][bc]==0 and arr[cr][cc]==0:
                # 배열 깊은 복사
                newarr = list()
                for i in range(R):
                    newarr.append(arr[i].copy())
                # 벽 3개 세우기
                newarr[ar][ac]=newarr[br][bc]=newarr[cr][cc]=1
                for i, j in virusRC:
                    dfs(i, j, newarr)
                
                # 안전구역 개수 세기
                cnt = 0
                for row in newarr:
                    cnt += row.count(0)
                answer = max(answer, cnt)
                
print(answer)