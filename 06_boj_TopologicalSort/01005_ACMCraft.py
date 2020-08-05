import sys
read = lambda : sys.stdin.readline().strip().split()
sys.setrecursionlimit(10**4)    # N=1000이므로 재귀호출 범위를 넉넉하게 잡아줄것

cache = list()      # 해당 건물까지 건설하는데 필요한 시간
D = list()          # 각 건물 짓는 시간
DAG = list()        # 2차원 행렬, 간선의 방향을 반대로 바꾼 그래프

def dfs(start):
    global cache

    # 더이상 갈 곳이 없으면
    if DAG[start].count(True) == 0:
        return D[start]
    elif cache[start] != -1:
        return cache[start]
    
    ret = 0
    for c, has_c in enumerate(DAG[start]):
        if has_c:
            ret = max(ret, dfs(c))
    
    cache[start] = ret + D[start]
    return ret + D[start]


T = (int)(input())
# 재귀로 풀어보자
for _ in range(T):
    # N, K 입력
    tmp = read()
    N = (int)(tmp[0])
    K = (int)(tmp[1])

    # 각 건물 건설 시간 입력
    D = [(int)(i) for i in read()]
    # 각 건물간 간선 입력
    # 단 간선 방향을 반대로 바꿔 저장한다 !!!
    DAG = list()
    for _ in range(N):
        DAG.append([False] * N)
    for _ in range(K):
        tmp = read()
        r = (int)(tmp[0]) - 1
        c = (int)(tmp[1]) - 1
        DAG[c][r] = True

    # 건설해야 하는 건물 번호 입력
    W = (int)(input()) - 1
    cache = [-1] * N
   
    # print('ret : ', dfs(W))
    print(dfs(W))
