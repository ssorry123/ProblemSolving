# 그리디 문제인 것을 모르고 문제만 봤을때
# 그리디를 사용하는 것이 좋다는 것을 알아낼 수 있을까?

# 최소스패닝트리, 크루스칼 알고리즘(탐욕적 선택기법)
# 스패닝 트리에는 싸이클이 존재하면 안된다
# 최소 비용간선을 선택하더라도, 싸이클이 생기면 선택하지 않는다

def find(me, ud):
    # 내가 대표이면
    if ud[me] == me:
        return me
    # 나의 대표를 찾아 떠난다
    root = find(ud[me], ud)
    ud[me] = root
    return root

def union(u, v, ud):
    if u==v:
        return
    if u>v:
        tmp = u
        u = v
        v= tmp
    
    a = find(u, ud)
    b = find(v, ud)
    ud[a] = b

def solution(n, costs):
    answer = 0
    ud = list()
    for i in range(n):
        ud.append(i)
    
    costs = sorted(costs, key = lambda x : x[2])
    print(costs)
    for u, v, w in costs:
        # u와 v를 연결했을때 싸이클이 생기는 경우
        a, b = find(u, ud), find(v, ud)
        if a==b:
            continue
        # u,v를 연결했을때 싸이클이 생기지 않는 경우
        answer += w
        # 두 노드를 연결한다(두 노드가 같은 그룹이 된다)
        union(a, b, ud)
        c, cnt = ud[0], 0
        # 모두 같은 그룹이면(최소 스패닝트리가 완성되었다면)
        for i in ud:
            if i==c:
                cnt+=1
        if cnt==n:
            break
    
    return answer