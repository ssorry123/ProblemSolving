# pypy3 612ms
# python3 4524ms

read = lambda : input().split()

class Node:
    def __init__(self, value):
        self.to_node = list()
        self.in_node_cnt = 0
        self.value = value

class Graph:
    nodes = dict()
    
    @classmethod
    def add_info(cls, r, c):
        """ int r, int c """
        r_node = c_node = None
        if r in cls.nodes:
            r_node = cls.nodes.get(r)
        else:
            r_node = Node(r)
            cls.nodes[r] = r_node
        
        if c in cls.nodes:
            c_node = cls.nodes.get(c)
        else:
            c_node = Node(c)
            cls.nodes[c] = c_node

        r_node.to_node.append(c)
        c_node.in_node_cnt = c_node.in_node_cnt + 1
        

a = read()
N = (int)(a[0])
M = (int)(a[1])

for _ in range(M):
    a = read()
    r = (int)(a[0])
    c = (int)(a[1])
    Graph.add_info(r, c)
# print(Graph.nodes)

# 혼자 있는 노드 출력, 어디에 있어도 상관 없음
alone = 0
for i in range(1,N+1):
    if not i in Graph.nodes:
        print(i, end=' ')
        alone += 1

Queue = list()
# discovered = [False] * (N + 1)
i=0
for key, node in Graph.nodes.items():
    # 들어오는 간선이 없을 경우 큐에 삽입한다
    if node.in_node_cnt == 0:
        Queue.append(key)
        # discovered[key] = True

# 혼자 있는 노드들을 제외한 두개 이상으로 연결된 노드들만 검사
N = N - alone
cnt = 0
while cnt < N:
    will_del = me = Queue.pop(0)
    print(me, end=' ')
    cnt += 1

    # 큐에서 꺼낸 노드에서 나가는 간선들을 제거한다
    me = Graph.nodes.get(me)
    #print(me)
    for i in me.to_node:
        tmp = Graph.nodes.get(i)
        tmp.in_node_cnt = tmp.in_node_cnt - 1
        
        # 간선을 제거한 후에 들어오는 간선이 0인 경우
        if tmp.in_node_cnt == 0:
            Queue.append(tmp.value)


    # 큐에서 꺼낸 노드는 필요 없다
    del Graph.nodes[will_del]

    """ 쓸데없이 for문을 두번 돌리지 않는다
    # # 이미 큐에 추가되지 않았고
    # # 들어오는 간선이 없을 경우 큐에 삽입한다
    # #print(Graph.nodes)
    # for key, node in Graph.nodes.items():
    #     if node.in_node_cnt == 0 and not discovered[key]:
    #         Queue.append(key)
    #         discovered[key] = True
    """


# N이 32000까지라서 N*N행렬과 N행렬을 만들면 메모리 초과가 나는 듯 하다
""" 
i_out = list()

for _ in range(N):
    i_out.append([False] * N)

for _ in range(M):
    a = read()
    r = (int)(a[0]) - 1
    c = (int)(a[1]) - 1
    # r에서 c로 나가는 간선이 있다
    i_out[r][c] = True

visited_cnt = 0
Queue = list()
visited = [False] * N

# 들어오는 간선이 없는 정점을 큐에 삽입
for c in range(N):
    no_in = True
    for r in range(N):
        if i_out[r][c]:
            no_in = False
            break
    if no_in:
        Queue.append(c)
        visited[c] = True


# 모든 정점을 검사할때까지 검사한다
while visited_cnt < N:
    # 한 점을 꺼낸다
    me = Queue.pop(0)
    print(me+1, end = ' ')
    visited_cnt += 1

    # 꺼낸 점에서 나가는 간선을 모두 제거한다
    for c in range(N):
        i_out[me][c] = False

    # 방문하지 않았고 들어오는 간선이 없는 정점을 큐에 삽입
    for c in range(N):
        if not visited[c]:
            no_in = True
            for r in range(N):
                if i_out[r][c]:
                    no_in = False
                    break
            if no_in:
                Queue.append(c)
                visited[c] = True """


#DFS 재귀방식으로 풀면 메모리 초과(재귀함수 깊어짐)
""" 
visited = [False] * N
ret = list()

def dfs(start):
    # int start
    visited[start] = True

    for i, col in enumerate(DAG[start]):
        # 방문할 수 있고, 방문하지 않았다면 방문한다
        if col and not visited[i]:
            dfs(i)
    
    # 자신이 시작한 깊이우선탐색이 완료되었을 경우
    # 자신을 자신이 재귀호출한 수들의 뒤에 추가한다
    ret.append(start)

# 모든 점들에 대해서 깊이 우선탐색을 실행한다
for i in range(N):
    if not visited[i]:
        dfs(i)

# 결과를 뒤집고 출력한다
ret.reverse()

for i in ret:
    print(i+1, end=' ')
 """
