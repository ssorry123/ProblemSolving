import math

def solution(n):
    answer = 0
    if n <= 2:
        return 1
    '''
    sum[1,i] = i(i+1)/2
    sum[a,b] = sum[1,b] - sum[1,a-1] = b(b+1)/2 - a(a-1)/2
             = (b+a)(b-a+1)/2
    '''
    '''
    (b+a)(b-a+1)/2 = n이 되는 a,b의 개수를 찾자
    (b+a)(b-a+1) = n*2  (b>=a)
    '''

    # b^2 + b - (2n + a^2 - a) = 0 
    # b = ( -1 + sqrt( 1+4(2n+a^2-a) ) ) / 2 ,, 근의공식
    for a in range(1, n+1):
        b_up = -1 + math.sqrt(1+4*(2*n+a**2 - a))
        if b_up <=0 or b_up % 2 != 0:
            continue
        b = b_up // 2
        if b < a:
            continue
        
        answer += 1

    return answer

for i in range(50):
    print(i, solution(i))