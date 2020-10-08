# AC
# 정삼각형 피라미드에서 가장 꼭대기에서 시작하여
# 반시계방향으로 나선형으로 돌며 순차적인 숫자를 입력하는 문제
# 규칙을 찾기 어려워 노가다 했다

# r, c에서 시작하여, 주어진 길이만큼 삼각형을 돌면서 채운다
def cover(r, c, start,_len, answer):
    # 아래로
    for rr in range(r, r+_len):
        answer[rr][c] = start
        start += 1
    
    # 오른쪽으로
    rr = r + _len -1
    for cc in range(c+1, c+1+_len-1):
        answer[rr][cc] = start
        start += 1
    
    # 대각선 위로
    r = r + _len - 2
    c = c + _len - 2
    cnt = 0
    while cnt < _len - 2:
        answer[r][c] = start
        start += 1
        r -= 1
        c -= 1
        cnt += 1
    
    # 채워야 할 수가 아직 남았다면
    # 다음 시작점의 좌표와, 매길 숫자의 시작 번호
    return r+2, c+1, start


def solution(n):
    answer = []

    # 채워야할 번호 1~number
    number = (n+1)*n//2

    # 피라미드 모양은, 계단 모양으로 구현
    for i in range(1, n + 1):
        answer.append([0]*i)
    
    # 일단 피라미드의 꼭대기에서 껍질 부분을 채운 후
    r, c, start = cover(0,0,1,n,answer)
    # number까지 채울때까지 계속 내부의 껍질을 채워 나간다
    # number까지 피라미드에 입력하였다면 종료
    while start <= number:
        n = n-3 # 껍질의 한 변의 길이는, 안으로 들어갈 수록 3씩 줄어든다
        r, c, start = cover(r, c, start, n, answer)

    # 결과는 하나의 리스트
    ret = answer[0]
    for i in range(1, len(answer)):
        ret += answer[i]

    return ret

solution(5)