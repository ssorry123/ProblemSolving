def solution(n):

    n = sorted(list(str(n)), reverse = True)
    
    ret = ''
    for i in range(len(n)):
        ret += n[i]

    return int(ret)


solution(118372)