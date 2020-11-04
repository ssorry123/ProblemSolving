def solution(s):
    answer = ''

    for i in range(len(s)):
        c = s[i]
        if c == ' ':
            answer += c
        # c가 첫 문자라면
        elif s[i-1] == ' ' or i==0:
            if c.isalpha():
                answer += c.upper()
            else:
                answer += c
        # 첫 문자가 아니라면
        else:
            if c.isalpha():
                answer += c.lower()
            else:
                answer += c


    return answer