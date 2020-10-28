# 수정해야함

import math


# 정확도 o, 효율성 x
def solution1(n, cores):
    answer = 0
    
    coresCnt = len(cores)
    
    time = 0
    endTimes = [0] * coresCnt
    
    while n>0:
        # 코어에 작업이 끝나있는지 보자
        for idx in range(coresCnt):
            # time 시점에, 코어의 작업이 끝나 새로운 작업을 받을 수 있는 경우
            if time >= endTimes[idx] and n>0:
                n-=1
                # idx 코어가 작업을 받고, 종료될 시간을 기록
                endTimes[idx] = time + cores[idx]
                answer = idx + 1
        time = sorted(endTimes)[0]
                
    return answer

print(solution(8, [1,2,3]))