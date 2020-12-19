# 트리에서 간선의 개수 = 항상 정점의 수 - 1
# 트리에서, 부모는 연결된 노드중 하나이거나 없음

import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

''' 입력 받기 '''
# N <= 100000, N^2 = 10,000,000,000,, 행렬로 트리를 나타내기엔 무리;
N, root, Q = map(int, read().split())   # Node 개수, root번호, 쿼리 개수

# 서로 연결됨을 표시
edge = dict()
for _ in range(N-1):
    u, v = map(int, read().split())
    if not u in edge:
        edge[u] = list()
    if not v in edge:
        edge[v] = list()
    
    edge[u].append(v)
    edge[v].append(u)


''' 트리 만들기 '''
Tree = dict()   # Tree[me] = [childs...],,   {자신 : 자식들}
def makeTree(me, parent):
    global Tree
    if not me in Tree:
        Tree[me] = set()    # 중복 입력은 없지만 중복된 자식 처리
    
    # 나와 연결된 노드 중에서
    for node in edge[me]:
        # 나의 부모가 아니면(트리의 부모는 연결된 노드 중 하나거나, 없다)
        if node != parent:
            Tree[me].add(node)      # 나의 자식으로 추가
            makeTree(node, me)      # 자식을 루트로 하는 서브트리 만들기
    return

# 트리 만들기
makeTree(root, -1)


''' 루트에서 내려가면서, 한번의 dfs로 모든 서브트리의 노드수를 파악 '''
cache = [0] * (N+1)
def countSubtree(me):
    global cache
    cache[me] = 1   # 자기 자신의 개수

    # 자식이 없으면, cache[me]=1로 종료된다
    for child in Tree[me]:
        countSubtree(child)         # 자식이 루트인 서브트리의 노드 개수를 센다
        cache[me] += cache[child]   # 자식 서브트리의 노드 개수 자기자신에 더해준다
    return

# 모든 서브트리의 노드 개수 구하기
countSubtree(root)


# 쿼리 처리하기
for _ in range(Q):
    query = int(read())
    print(cache[query])