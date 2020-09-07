# 분으로만 표현된 시간을 "hh:mm"으로 반환
def mm_to_hhmm(mm):
    hh = str(mm // 60)
    mm = str(mm % 60)
    hh = hh if len(hh)==2 else '0'+hh
    mm = mm if len(mm)==2 else '0'+mm
    return hh+':'+mm

def solution(n, t, m, timetable):
    answer = ''
    
    tmp = list()                    # 버스를 타기위해 기다리고 있는 사람들의 도착 시간
    last_bus_mm = 60*9 + (n-1)*t    # 막차 버스 시간

    for t_str in timetable:
        hh, mm = t_str.split(':')
        mmmm = int(hh)*60 + int(mm) # 분으로 모두 변경
        # 막차보다 늦게(크게) 도착하는 사람들은 제외
        if mmmm <= last_bus_mm:
            tmp.append(mmmm)

    # 내림차순 정렬(제거할때 효율성을 위해)
    tmp = sorted(tmp, reverse=True)
    
    # 게으른 콘은 무조건 막차를 타야 가장 늦게 도착할 수 있다
    # 막차 전까지 모두 태우고 생각해 보자, 막차 = 9시 + (n-1)*t
    # (참고 : 입출력 예제 두번째)
    for i in range(n - 1):
        bus_t = 9*60+  (i * t)  # 첫차부터, 막차전까지 버스 시간
        print(mm_to_hhmm(bus_t))
        cnt = 0
        # 버스가 도착했을때 m명이 차지 않은 경우
        while cnt < m:
            # 기다리는 사람이 있고, 탈 사람이 버스 도착시간보다 같거나일찍온경우
            if len(tmp) > 0 and tmp[-1] <= bus_t:
                del tmp[-1]
                cnt += 1
            else:
                break
    

    # 이제 버스는 막차 한대 남았고, 버스는 m명까지 태울 수 있다
    ''' 대기열에 m명보다 적게 있으면, 막차 시간에 맞춰 정류장에 도착하면 된다 '''
    if len(tmp) < m:
        return mm_to_hhmm(last_bus_mm)

    ''' 대기열에 m명 이상 있는 경우 '''
    # 처음 tmp배열에 last_bus_mm보다 큰 값은 넣지 않았으므로
    # 남은 경우의 tmp[-m] 값은 <= last_bus_mm이다,
    # tmp[-m]의 값보다 같거나 큰 시간에 도착하면, 순위가 -(m+1)이 되므로 탈 수 없다
    # 가장 늦게 도착하려면, tmp[-m]보다 1분 일찍 도착하면 된다
    return mm_to_hhmm(tmp[-m]-1)
