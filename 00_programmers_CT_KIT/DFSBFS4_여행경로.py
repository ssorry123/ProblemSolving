def dfs(here, air, answer):
    ret = 0
    for u in air:
        ret += len(air[u])
    # 모든 티켓을 사용한 경우
    if ret == 0:
        return True

    # 이거 안해줘서 계속 에러났음
    # 마지막 공항에서 다른 공항으로 가는 항공편이 아예 없는 경우임
    # 애초에 (마지막공항->다른 공항) 이라는 티켓이 없던 경우
    if not here in air:
        return False
    
    for idx, there in enumerate(air[here]):
        air[here].pop(idx)  # 티켓 제거
        answer.append(there)
        tmp = dfs(there, air, answer)     # 방문    
        if tmp:
            return True
        answer.pop()
        air[here].insert(idx, there)    # 티켓 추가
    
    return False

def solution(tickets):
    answer = []
    
    air = dict()
    # 입력 받기
    for u, v in tickets:
        if not u in air:
            air[u] = list()
        air[u].append(v)
    # 알파벳 순 정렬
    for u in air:
        air[u] = sorted(air[u])

    
    answer.append('ICN')
    dfs('ICN', air, answer)
    
    print(answer)
    
    return answer

solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "D"], ["D", "A"]])