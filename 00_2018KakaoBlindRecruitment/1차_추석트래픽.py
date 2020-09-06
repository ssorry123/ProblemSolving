def fminusf(a, b):
    # 두수의 차가 0.001보다 작으면
    # 두 수는 같다고 처리
    if abs(a-b)<0.001:
        return 0
    return a-b

def solution(lines):
    answer = 0
    # 각 트래픽의 시작 시간과 종료 시간을 저장
    start_end = []
    for l in lines:
        aa, bb, cc = l.split()
        duration = float(cc[:-1])   # 트래픽 처리하는데 걸리는 시간
        hh, mm, ss = bb.split(':')  # 모두 초로 변경하고 저장
        endtime = float(hh)*60*60 + float(mm)*60 + float(ss)
        start_end.append([endtime - duration + 0.001, endtime])
    
    # 시작 시간을 기준으로 정렬
    start_end = sorted(start_end, key = lambda x:x[0])

    onCPU = []  # 시작시간을 기준으로 cpu에 적재
    # 한 트래픽이 cpu에 적재되면 해당 시간을 기준으로
    # 자신 포함 1초전까지 실행되고 있던 트래픽의 개수를 카운팅

    # 트래픽이 cpu에 적재되는 순간에 1초간 실행중이었던 트래픽들의 수가 증가될 수 있고,
    # 1초간 처리한 트래픽의 수의 최대를 알고싶다면 적재되는 순간이 1초구간의 끝부분이 되어야함

    for traffic in start_end:
        s, e = traffic
        cnt = 1 # 자기 자신
        ss = s - 0.999
        # 1초 구간 [ss, s]
        for oncpu in onCPU:
            # 먼저 적재된 트래픽의 종료시간이 ss보다 크거나 같은 경우
            # 즉 ss시간에 아직 끝나지 않고 실행중인 경우
            if fminusf(ss, oncpu) <= 0:
                cnt += 1
        
        onCPU.append(e) # 자기 자신의 종료시간만 기록

        answer = max(answer, cnt)
    
    print(answer)
    return answer

# solution([
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ])

# solution([
# '2016-09-15 20:59:57.421 0.351s',
# '2016-09-15 20:59:58.233 1.181s',
# '2016-09-15 20:59:58.299 0.8s',
# '2016-09-15 20:59:58.688 1.041s',
# '2016-09-15 20:59:59.591 1.412s',
# '2016-09-15 21:00:00.464 1.466s',
# '2016-09-15 21:00:00.741 1.581s',
# '2016-09-15 21:00:00.748 2.31s',
# '2016-09-15 21:00:00.966 0.381s',
# '2016-09-15 21:00:02.066 2.62s'
# ])