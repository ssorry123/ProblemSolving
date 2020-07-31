a = [(int)(i) for i in input().split()]
N = a[0]
M = a[1]
V = a[2] - 1

# 초기 그래프. 모두 0
graph = list()
for _ in range(N):
    graph.append([0]*N)

# 그래프 정보 업데이트
# 점의 번호가 1부터 시작하므로 1을 빼준후 결과를 출력할때 1을 더해주자
for _ in range(M):
    a = [(int)(i) for i in input().split()]
    row = a[0]-1
    col = a[1]-1
    graph[row][col] = graph[col][row] = True


# DFS
visited = list()
for _ in range(N):
    visited.append(False)
def DFS(start):
    global visited
    visited[start] = True
    print(start+1, end=' ')
    for i, col in enumerate(graph[start]):
        # 연결되어 있고 방문하지 않은 경우
        if (col) and (not visited[i]): 
            DFS(i)

DFS(V)
print('')

# BFS
discovered = list()
for _ in range(N):
    discovered.append(False)
Queue = list()

def BFS(start):
    global visited
    # 시작 원소 방문할 목록에 추가
    discovered[start] = True
    Queue.append(start)

    while len(Queue) > 0:
        # 방문했다고 알림
        start = Queue.pop(0)
        print(start + 1, end=' ')

        for i, col in enumerate(graph[start]):
            # 연결되어 있고 방문하지 않은 경우 다음에 방문할 목록에 추가
            if (col) and (not discovered[i]): 
                discovered[i] = True
                Queue.append(i)
                


BFS(V)
print('')