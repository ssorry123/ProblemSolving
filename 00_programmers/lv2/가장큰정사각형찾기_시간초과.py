MAX_SIZE = 0
max_size = 1    # 현재까지 구한 가장 큰 정사각형 크기
call_count = 0

def find(r, c, board):
    global max_size, MAX_SIZE
    # 자기 자신 크기
    # ret = 1
    row = len(board)
    col = len(board[0])

    # 가장 큰 정사각형보다 더 큰 정사각형(1더큰)을 찾을 수 있는가?
    if r + max_size >= row or c + max_size >= col:
        return 1
    
    # 가장 큰 정사각형보다 1더큰 정사각형이 존재하는가?
    for nr in range(r, r + max_size + 1):
        for nc in range(c, c + max_size + 1):
            if board[nr][nc] == 0:
                return 1
    
    # ret = max_size + 1
    max_size += 1

    # 한줄씩 더 만들어 보자
    next_row = r + max_size
    next_col = c + max_size
    while next_row < row and next_col < col:
        stop = False
        for nc in range(c, next_col):
            if board[next_row][nc] == 0:
                stop = True
                break
        if stop:
            break

        for nr in range(r, next_row):
            if board[nr][next_col] == 0:
                stop = True
                break
        if stop:
            break
        
        # ret += 1
        max_size += 1
        next_row += 1
        next_col += 1

    return max_size

def solution(board):
    answer = 1

    # 한점을 정사각형의 왼쪽위꼭지점이라 생각하고
    # 확장해나가자

    global MAX_SIZE, max_size, call_count
    MAX_SIZE = min(len(board), len(board[0]))
    max_size = 1

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != 0:
                find(r, c, board)
                call_count += 1

    if call_count==0:
        return 0

    answer = max_size * max_size
    return answer