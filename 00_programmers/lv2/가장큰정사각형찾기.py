# 레벨 2가 레벨 3보다 어려운거 같다
'''
DP 문제,,
각 점을, 각 점을 오른쪽아래 꼭지점으로 할때
만들 수 있는 가장 큰 정사각형의 크기라고 정의

0인 경우, 0크기의 정사각형을 만들 수 있다
1인 경우, 1크기의 정사각형을 만들 수 있다
초기에는 0, 1 상태
다르게 표현하면, 3인 경우 자신이 정사각형의 오른쪽아래 점이 되어
3*3에는 모두 1이 있다는 뜻이다.

위,왼쪽,대각선왼쪽 모두 1이고, 자기자신도 1이라면, 4개를 합쳐
한 변의 길이가 2인 정사각형을 만들 수 있다,

- ex : 모두 3이어야 4를 만들 수 있다
- 3개의 값중 가장 작은 값 + 1 ==> 만큼의 정사각형을 만들 수 있다

'''

def solution(board):
    # ex) [[0,0,0,0,0,0,,,, ... ,,, 0,0,0,0,]]
    if len(board)==1:
        if board[0].count(1) == 0:
            return 0
        return 1
    # ex) [[0],[0],[0],[0],[0],[0],[0],,,, [0],[0],[0]]
    if len(board[0])==1:
        for i in range(len(board)):
            if board[i][0]==1:
                return 1
        return 0

    answer = 0
    # 가장 윗줄, 가장왼쪽 줄은 더이상 확장할 수 없다
    # (확장 : 위, 왼쪽, 대각선왼쪽으로 확장)
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            if board[r][c] == 1:
                board[r][c] = min([board[r-1][c], board[r][c-1], board[r-1][c-1]]) + 1
                answer = max(answer, board[r][c])

    return answer * answer

solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]])