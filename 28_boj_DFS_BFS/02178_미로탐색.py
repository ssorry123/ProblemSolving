import sys
read = lambda : sys.stdin.readline().strip()
a = read().split()
N = (int)(a[0])
M = (int)(a[1])

miro = list()
for _ in range(N):
    miro.append(read())
# print(miro)

discovered = list()
for _ in range(N):
    discovered.append([False]*M)
# print(discovered)
Queue = list()

def BFS(start_row=0, start_col=0, end_row=N-1, end_col=M-1):
    # 발견했다고 표시, 다음에 방문할 목록에 포함
    discovered[start_row][start_col] = True
    Queue.append([start_row, start_col, 1])

    while len(Queue)>0:
        me = Queue.pop(0)
        me_row = me[0]
        me_col = me[1]
        me_depth = me[2]

        # 도착했을 경우
        if me_row == end_row and me_col == end_col:
            print(me_depth)
            break

        # 아래로 한칸
        if (me_row + 1 < N)\
                and (not discovered[me_row + 1][me_col])\
                and (miro[me_row + 1][me_col] == '1'):
            discovered[me_row + 1][me_col] = True
            Queue.append([me_row + 1, me_col, me_depth + 1])
        # 위로 한칸
        if (me_row - 1 >=0)\
                and (not discovered[me_row - 1][me_col])\
                and (miro[me_row - 1][me_col] == '1'):
            discovered[me_row - 1][me_col] = True
            Queue.append([me_row - 1, me_col, me_depth + 1])

        # 오른쪽으로 한칸
        if (me_col + 1 < M)\
                and (not discovered[me_row][me_col + 1])\
                and (miro[me_row][me_col + 1] == '1'):
            discovered[me_row][me_col + 1] = True
            Queue.append([me_row, me_col + 1, me_depth + 1])
        
        # 왼쪽으로 한칸
        if (me_col - 1 >= 0)\
                and (not discovered[me_row][me_col - 1])\
                and (miro[me_row][me_col - 1] == '1'):
            discovered[me_row][me_col - 1] = True
            Queue.append([me_row, me_col - 1, me_depth + 1])

BFS()