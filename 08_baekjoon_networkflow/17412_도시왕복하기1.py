import sys
read = lambda : sys.stdin.readline().strip().split()

a = read()
N = (int)(a[0])
P = (int)(a[1])

capacity = list()
flow = list()
for _ in range(N+1):
    capacity.append([0]*(N+1))
    flow.append([0]*(N+1))

for _ in range(P):
    a = read()
    r = (int)(a[0])
    c = (int)(a[1])
    # 오답 원인
    # capacity[r][c] = capacity[c][r] =1
    capacity[r][c] =1

def index_0(LIST, col):
    '''
    N*2배열의 원소 (row, col) 중에서
    인자 col과 값이 일치하는 col의 row를 반환
    '''
    for i, row in enumerate(LIST):
        if row[1] == col:
            return row[0]
    
    return -1

ret = 0
def netFlow(source = 1, sink = 2):
    global capacity, flow, ret

    run = True
    while run:
        # BFS로 최단 증가경로 찾기
        # 시작점을 큐에 넣고 시작, 부모 표시
        Queue = list()
        Queue.append([0, source])   # 출발 지점 source, 가상의 0
        visited = [False] * (N+1)
        visited[source] = True
        Shortpass = list()
        has_STP = False
        while len(Queue) > 0 and not has_STP:
            me = Queue.pop(0)
            Shortpass.append(me)
            # me와 한칸씩 떨어져 있는 것들
            for col_i in range(1,N+1):
                # 간선의 용량 - 간선에 흐르고 있는 양 = 남은 양
                if capacity[me[1]][col_i] - flow[me[1]][col_i] > 0\
                        and not visited[col_i]:
                    # BFS로 노드가 아닌 간선을 추가
                    Queue.append([me[1], col_i])
                    visited[col_i] = True
                    # 최단 경로를 찾은 경우
                    # 찾았다고 while을 종료시켜버리면 마지막 경로를
                    # 자기 자신을 ShortPass에 추가시키지 않는다
                    # 최단 경로를 하나 찾은경우 일단 더 찾아볼 필요는 없다
                    if col_i == sink:
                        has_STP = True
                        Shortpass.append([me[1], col_i])
                        break

        if has_STP:
            FirstPass = list()
            index = sink
            while index > 0:
                x_index = index
                index = index_0(Shortpass, x_index)
                # index or x_index가 0인경우는 신경 안써도됨

                # 한 경로에 보낼 용량은 1로 정해져 있음
                flow[index][x_index] += 1
                flow[x_index][index] -= 1
                FirstPass.insert(0, x_index)
            ret += 1
            run = True
        else:
            run = False


netFlow()
print(ret)

