def solution(n):
    answer = ''

    if n%2 == 0:
        return '수박' * (n//2)
    
    return '수박' * ( (n-1) // 2 ) + '수'
