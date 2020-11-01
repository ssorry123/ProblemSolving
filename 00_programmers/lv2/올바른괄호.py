def solution(s):
    answer = True
    
    if len(s) % 2 == 1:
        return False
    
    cnt = 0

    for i in range(len(s)):
        c = s[i]
        if c == '(':
            cnt += 1
        else:
            if cnt==0:
                return False
            cnt -= 1 

    if cnt != 0:
        return False

    return True