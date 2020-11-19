from collections import Counter

def solution(s):

    # 대소문자를 비교하지 않습니다, 소문자로 통일
    s = s.lower()

    # 각 알파벳 문자수 세기
    d = dict(Counter(s))

    # p와 또는 y가 문자열에 없는 경우
    if not 'p' in d or not 'y' in d:
        return False

    if d['p'] == d['y']:
        return True
    else:
        return False
    
    return True
