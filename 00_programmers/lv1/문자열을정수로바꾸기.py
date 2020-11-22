def solution(s):
    # 부호가 없는 숫자면
    if s[0] != '-' and s[0] != '+':
        return int(s)
    
    # 부호가 있는 숫자면
    ret = int(s[1:])

    if s[0] == '-':
        return -ret
    else:
        return ret
