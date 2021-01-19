# 하향식(메모이제이션) DP..?

cache = dict()

def dfs(r, c, tri):
    global cache

    # 바닥에 도착한 경우
    if r == len(tri)-1:
        return tri[r][c]

    if (r,c) in cache:
        return cache[(r,c)]

    # 자식 두명(어떤 경우는 한명)
    # 부터 단말까지 내려갔을때, 가장 큰 값을 리턴
    a = dfs(r+1, c, tri)
    b = -1
    if c+1 <= r+1:
        b = dfs(r+1, c+1, tri)

    # 자식부터 단말가지 내려갔을때 가장 큰값 + 자신의 값 리턴
    ret = max(a, b)
    ret += tri[r][c]
    cache[(r,c)] = ret
    return ret



def solution(triangle):
    answer = 0

    answer = dfs(0,0,triangle)

    return answer