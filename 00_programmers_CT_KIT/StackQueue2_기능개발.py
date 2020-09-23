import math

def solution(progresses, speeds):
    answer = []
    N = len(speeds)

    day = [0] * N   # 각 기능이 완성되는데 걸리는 시간
    for i in range(N):
        day[i] = math.ceil((100-progresses[i]) / speeds[i])
    # print(day)

    out = list()    # 배포 대기중

    for i in range(len(day)):
        # 비어있는 경우, 그냥 추가
        if len(out) == 0:
            out.append(day[i])

        # 등록된 배포 일정보다 일찍 끝나는 경우, 대기함
        elif out[0] > day[i]:
            out.append(day[i])

        # 등록된 배포일정과 같이 완성되는 경우, 배포해버리면 좋겠지만,,
        # 뒤의 기능도 같이 완성될 수도 있으므로, 일단 대기
        elif out[0] == day[i]:
            out.append(day[i])
            
        # 대기중인 모든 배포를 진행함
        else:
            answer.append(len(out))
            out.clear()
            out.append(day[i])

    # 남은 배포를 처리함
    if len(out)!=0:
        answer.append(len(out))
        
     
    return answer

print(solution([93, 30, 55], [1, 30, 5]))