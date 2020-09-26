# 맨해튼 거리
# 고딩때 많이 풀던게, DP였다니

map = list()
MOD = 1000000007

def solution(C, R, puddles):
    answer = 0
    # m=col, n = row

    ### making map
    global map  # use 1~
    map = list()
    # 0번 라인은 패딩
    for r in range(R+1):
        map.append([0]*(C+1))
    
    ### add puddles,
    for r, c in puddles:
        map[c][r] = -1  # 주의! 주어지는 좌표는 (c, r)이다

    # 초기화
    map[1][1] = 1

    # DP
    for r in range(1, R+1):
        for c in range(1, C+1):
            # 초기화된 지역이거나, 물웅덩이인 경우
            if map[r][c] == 1 or map[r][c] == -1:
                continue

            # 현재 위치까지 오는 경로의 수 -> 위에서 내려오기 + 왼쪽에서 오기
            up = map[r-1][c] 
            left = map[r][c-1]
            up = 0 if up==-1 else up
            left = 0 if left==-1 else left
            map[r][c] = (up+left) % MOD # 여기서 % 안해주도 됨


    return map[R][C] % MOD

solution(4,3,[[2,2]])