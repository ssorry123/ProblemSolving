def solution(words, queries):
    answer = []
    # 트라이 미사용, string slice
    # 효율성테스트 2번만 시간초과

    # 단어 길이에 따른 분류
    by_len = dict()
    for w in words:
        key = len(w)
        if key in by_len:
            by_len[key].append(w)
        else:
            by_len[key] = list()
            by_len[key].append(w)

    # 메모이제이션용 변수
    cache = dict()

    for q in queries:
        # 메모이제이션
        if q in cache:
            answer.append(cache[q])
            continue
        # 쿼리의 길이에 맞는 단어가 없을 경우
        if not len(q) in by_len:
            answer.append(0)
            continue

        ''' 매치되는지 확인 '''
        # ?가 앞인지 뒤인지 확인
        front = True
        if q[-1] == '?':
            front = False
        # 길이 확인        
        key = len(q)
        # ?가 몇글자인지 확인
        wildcard_cnt = q.count('?')

        cnt = 0
        # 와일드카드부분을 제거한 문자열 비교
        for w in by_len[key]:
            if front:
                if w[wildcard_cnt:] == q[wildcard_cnt:]:
                    cnt += 1
            else:
                if w[:-wildcard_cnt] == q[:-wildcard_cnt]:
                    cnt += 1

        answer.append(cnt)
        cache[q] = cnt  # 메모이제이션

    return answer

print(
    solution(
        ["frodo", "front", "frost", "frozen", "frame", "kakao"],
        ["fro??", "????o", "fr???", "fro???", "pro?"]
    )
)