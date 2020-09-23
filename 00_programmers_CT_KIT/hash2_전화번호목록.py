def solution(phone_book):
    answer = True

    # 길이가 짧은 것 문자열이 긴 문자열의 접두어가 될 가능성이 있다
    p = sorted(phone_book, key = lambda x:len(x))   # 길이가 짧은 것 우선으로 정렬
    len_p = len(p)

    for idx, s in enumerate(p):
        s_len = len(s)
        for i in range(idx+1, len_p):
            if s == p[i][:s_len]:
                return False


    return answer

