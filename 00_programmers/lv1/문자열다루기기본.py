def solution(s):
    
    # 길이가 4 또는 6인 문자열이
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True

    return False


