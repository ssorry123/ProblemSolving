# 한 명이 건너갈떄마다, 모든 돌의 숫자가 1씩 줄어든다
# 내구도가 줄어든다고 생각하면 될듯
# 내구도가 0이되서, 돌맹이가 사라지면
# 사라진 돌맹이의 길이가 k개보다 작다면 점프할 수 있꼬
# k와 같거나 크다면 점프할 수 없다

# 어찌 되었든 모든 돌들을 밟고 지나간다고 생각하면
# 한명이 지나갈때마다 1씩 감소하는 방법으로 하면 시간초과가 날것
# (stones배열은 크기가 매우 큼)

# a명이 지나갔다면, 모든 돌들의 숫자는 -= a 가 되어있을 것
# 음수인 돌들은 0인 상태에서 점프를 당한 돌들 일것이다
# 0인 경우는 밟은 후에 0이 된것이므로 ㄱㅊ다
# 0에서 음수로 된경우가 k개 이상 연속되어 있다면, 건널 수 없는데 a명이 건넌것이다

def solution(stones, k):
    answer = 0

    left = 0            # 건널 수 있는 최소 사람 수
    right = max(stones) # 모든 돌들이 max값과 같다면, max값만큼 건널 수 있다

    # 2분탐색
    while left <= right:
        # mid명을 통과시킴
        mid = (left+right)//2

        seq_minus_cnt = 0
        ret = True
        for s in stones:
            if s - mid < 0:
                seq_minus_cnt += 1  # 연속되는 -개수 구하기
            else:
                seq_minus_cnt = 0   # 연속되는 -개수 초기화
            
            # k개 이상 연속되는 -가 존재한다면
            if seq_minus_cnt >= k:
                ret = False
                break
        
        # mid명이 지나갈 수 있다면, 더 지나가게 해보자
        if ret:
            answer = mid
            left = mid + 1
        # 지나갈 수 없다면, 적게 지나가게 해보자
        else:
            right = mid - 1

    return answer
