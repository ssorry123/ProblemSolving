cache = list()  # 방문 여부 기록

def dfs(start, com):
    global cache
    cache[start] = True
    
    # 연결된 컴퓨터가 없다면
    if com[start].count(1) == 1:
        return
    
    for i in range(len(com)):
        # 연결되어 있고, 자기 자신이 아니고, 방문하지 않은 경우
        if com[start][i]==1 and i!=start and cache[i]==False:
            dfs(i, com)
    
    return


def solution(n, computers):
    global cache
    answer = 0
    
    # 캐시 초기화
    cache = [False] * len(computers)
    
    # 그래프의 모든 노드 탐색
    for i in range(len(computers)):
        if cache[i] == False:
            dfs(i, computers)
            answer += 1
    
    return answer