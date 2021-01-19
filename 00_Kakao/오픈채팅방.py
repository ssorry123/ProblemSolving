def solution(record):
    answer = []
    log = dict()    # {uid : nick}
    # user의 최종 nick만 알고 있으면 됨
    for rec in record:
        tmp = rec.split()   # 띄어쓰기로 나누기
        op, uid = tmp[0], tmp[1]
        # 들어오거나 나가는 경우, 해당 uid의 nick 업데이트
        if op == 'Enter' or op == 'Change':
            log[uid] = tmp[2]
    
    # 정답 출력
    for rec in record:
        tmp = rec.split()
        op, uid = tmp[0], tmp[1]
        if op == 'Enter':
            answer.append(log[uid] + '님이 들어왔습니다.')
        elif op == 'Leave':
            answer.append(log[uid] + '님이 나갔습니다.')
        else:
            continue

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))