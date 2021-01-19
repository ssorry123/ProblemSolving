def solution(msg):
    answer = []

    d = dict()  # key : word, val : int
    i = 1
    for k in range(26):
        d[chr(ord('A') + k)] = i
        i += 1
    
    idx = 0
    while idx < len(msg):
        w = msg[idx]
        for ap in range(idx + 1, len(msg)):
            # 사전에 존재하면
            if w + msg[ap] in d:
                w += msg[ap]
            # 사전에 존재하지 않으면
            else:
                break

        # 출력
        answer.append(d[w])

        # 사전에 추가할 단어 만들기 준비
        ap = idx + len(w)
        # 추가할 단어가 없다면 종료
        if ap >= len(msg):
            break

        # 사전에 단어 추가
        d[ w + msg[ap] ] = i
        i += 1

        # 다음 단어로 이동
        idx = ap
    
    return answer

solution('KAKAO')
solution('TOBEORNOTTOBEORTOBEORNOT')