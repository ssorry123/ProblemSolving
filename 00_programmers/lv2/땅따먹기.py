import sys
sys.setrecursionlimit(10**9)


# i번째부터 끝까지 선택했을때
# 가장 합이 큰 것을 리턴
cache = list()
def dfs(level, before_choice, land):
    if level == len(land):
        return 0
    #
    if cache[level][before_choice] != -1:
        return cache[level][before_choice]
    

    ret = -1
    for choice in range(4):
        if choice != before_choice:
            # (자기 자신값 + 뒤에서 선택한 값) 가장 큰 값을 저장
            tmp = land[level][choice] + dfs(level+1, choice, land)
            ret = max(ret, tmp)
    
    cache[level][before_choice] = ret
    return ret


def solution(land):
    answer = 0

    N = len(land)
    global cache
    cache = list()
    for _ in range(N):
        cache.append([-1, -1, -1, -1])

    answer = dfs(0, -1, land)

    return answer