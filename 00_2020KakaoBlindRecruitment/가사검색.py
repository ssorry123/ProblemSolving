def solution(words, queries):
    answer = []
    # 효율성도 본다고 하니, 해쉬처럼, 단어의 길이에 따라 리스트를 만들어보자
    # 효율성테스트 2번 실패,,
    by_len = dict()
    for w in words:
        key = len(w)
        if key in by_len:
            by_len[key].append(w)
        else:
            by_len[key] = list()
            by_len[key].append(w)

    # 중복된 쿼리에 대한 처리
    cache = dict()

    for q in queries:
        ''' 메모이제이션 '''
        if q in cache:
            answer.append(cache[q])
            continue

        # ?가 앞인지 뒤인지 확인
        front = True
        if q[-1] == '?':
            front = False


        ''' 매치되는지 확인 '''
        key = len(q)
        # 쿼리 길이에 맞는 워드가 없는 경우
        if not key in by_len:
            answer.append(0)
            continue
        
        # 해당 쿼리의 길이에 해당하는 단어가 존재할 경우
        cnt = 0
        
        # ?가 몇글자인지 확인
        wildcard_cnt = q.count('?')

        # 와일드카드부분을 제거한 문자열 추출
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

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                ["fro??", "????o", "fr???", "fro???", "pro?"]
            )
)