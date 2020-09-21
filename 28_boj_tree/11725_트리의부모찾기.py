import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()

### input
N = int(read()) # 노드의 개수

# 트리의 루트는 1번 노드
# Node 객체
class Node:
    def __init__(self):
        self.adj = []

# Tree 배열, index는 노드의 번호
Tree = [0]*(N+1)    # use [1,N]
for i in range(1, N+1):
    Tree[i] = Node()

for _ in range(N-1):
    # a, b 노드는 연결되어 있음
    a, b= map(int, read().split())
    Tree[a].adj.append(b)
    Tree[b].adj.append(a)

### start solution
ret = [0]*(N+1)             # 노드의 부모 저장 배열
visited = [False] * (N+1)   # 방문 확인

# dfs로, 트리의 모든 노드를 탐색한다
def dfs(here = 1):
    global N, ret, visited, tree
    visited[here] = True

    # 연결된 노드중, 방문하지 않은 노드라면 방문
    for there in Tree[here].adj:
        if visited[there] == False:
            ret[there] = here   # 방문할 노드there의 부모는 here
            dfs(there)
    
dfs(1)
for i in range(2, N+1):
    print(ret[i])