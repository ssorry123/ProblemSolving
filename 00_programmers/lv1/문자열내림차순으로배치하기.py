def solution(s):
    answer = ''

    # 문자열이 각각 문자로, 배열로 분리 됨
    tmp = list(s)
    # print(tmp)

    # 문자를 큰 것부터 작은 순으로 정렬

    # 소문자 유니코드 < 대문자 유니코드

    tmp = sorted(tmp, key = lambda x : -ord(x))
    for t in tmp:
        answer += t

    return answer
