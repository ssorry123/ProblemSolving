# 사이즈가 작아서 전체탐색해도 괜찮을 것 같다

# bid에 해당하는 uid인지 확인
def check(bid, uid):
    if len(bid) != len(uid):
        return False
    
    for i in range(len(bid)):
        if bid[i] == '*':
            continue
        if bid[i] != uid[i]:
            return False
    # print(bid, uid)
    return True
    

log = []
def dfs(b_idx, b_to_u, user_id, visited, answer_set):
    if b_idx == len(b_to_u):
        tmp = tuple(sorted(log))
        answer_set.add(tmp)
        # print(tmp)
        return
    
    for uid in b_to_u[b_idx]:
        uid_idx = user_id.index(uid)
        if not visited[uid_idx]:
            visited[uid_idx] = True
            log.append(uid)
            dfs(b_idx + 1, b_to_u, user_id, visited, answer_set)
            log.pop(-1)
            visited[uid_idx] = False


def solution(user_id, banned_id):
    # 각각의 banned_id에 대해서, 매칭되는 user_id를 저장
    b_to_u = list()
    for _ in range(len(banned_id)):
        b_to_u.append([])

    for i in range(len(banned_id)):
        bid = banned_id[i]
        for j in range(len(user_id)):
            uid = user_id[j]
            if check(bid, uid):
                b_to_u[i].append(uid)

    print(b_to_u)
    # 하나의 bid에 대해서, 하나의 uid와 매칭된다
    # b_to_u는 각 bid가, 선택할 수 있는 uid 목록들이다
    # 완전 탐색을하지만, 이전 bid중에 이미 선택한 uid가 있다면
    # 선택할 수 없다

    # 문제는 각각의 bid가 uid를 선택하는 순서는 상관이 없다는 것이다
    # 3개의 bid가 (a,b,c)를 선택하든 (b, a, c)를 선택하든 
    # uid가 제제되는 같은 경우이다,,

    global log
    visited = [False] * len(user_id)
    answer_set = set()
    log = []
    dfs(0, b_to_u, user_id, visited, answer_set)
    
    answer = len(answer_set)

    return answer

