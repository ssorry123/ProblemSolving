def check(R, C, board):
    ''' bool값 ,보드의 한 상태에서 삭제되어야할 2*2의 3사분면 리스트 반환 ''' 
    willDel = list()
    for r in range(C-1):
        for c in range(R-1):
            # 2*2 검사
            ablock = board[r][c]
            # 3사분면 블록이 빈칸이 아니고 2*2가 같은 캐릭터인 경우
            if ablock == board[r][c+1] and\
                ablock == board[r+1][c] and\
                    ablock == board[r+1][c+1] and\
                        ablock != -1:
                # 삭제할 목록에 3사분면좌표 추가
                willDel.append([r,c])
    
    # 삭제할 캐릭터가 없는 경우
    if len(willDel)==0:
        return False, []
    # 삭제할 블록들이 있는 경우
    else:
        return True, willDel

def del22(r, c, b):
    ''' 3사분면 기준 2*2 블록들 제거, 실제로 제거한 블록수 리턴'''
    cnt = 4
    # 이미 삭제된 경우
    if b[r][c] == -1:
        cnt -= 1
    if b[r+1][c] == -1:
        cnt -= 1
    if b[r][c+1] == -1:
        cnt -= 1
    if b[r+1][c+1] == -1:
        cnt -= 1
    b[r][c] = b[r+1][c] = b[r+1][c+1] = b[r][c+1] = -1
    return cnt


def downBoard(height, board):
    ''' 중력으로 빈칸 내리기 '''
    for i, col in enumerate(board):
        col = [c for c in col if c!=-1] # -1이 아닌 것들만 다시 저장
        while len(col) < height:        # 부족한 높이는 -1(빈칸)로 채우기
            col.append(-1)
        board[i] = col                  # 새로 만든 board로 치환

def solution(R, C, board):
    answer = 0
    # 보드를 가로 맨 아랫줄의 컬럼이 각각 list의 시작점이 되도록 수정
    # 기존 ->
    # 00,01,02,0C
    # 10,11,12,1C
    # ....
    # R0,R1,R2,RC
    # 수정 후 (실제론c-1, r-1까지) ->
    # 수학에서 익숙한 x,y 좌표 개념
    # 0R 1R 2R 3R....CR
    # .................
    # 01 11 21 31......
    # 00 10 20 30....C0
    new_board= list()
    for c in range(C):
        new_board.append([])
        for r in range(R-1, -1, -1):
            new_board[c].append(board[r][c])
    board = new_board

    # 삭제할 칸들이 있다면 계속 삭제
    # 한번 삭제할때 한꺼번에 삭제하고, 맵을 갱신해야 함
    while True:
        haveDel, delList = check(R, C, board)
        
        # 삭제할 것이 없다면 종료
        if not haveDel:
            break
        
        # 삭제할 것이 있다면 삭제
        for r, c in delList:
            answer += del22(r, c, board)
        
        # 중력으로 내리기(맵 갱신하기)
        downBoard(R, board)

    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))