''' 대회 당시 AC ''' 

import math
# 주어진 10진수 n을 3진수로 변환하고
# 변환된 3진수를 reverse한 후
# reverse한 3진수를 10진수로 표현하는 문제
def solution(n):
    answer = 0

    ret = ''

    while n!=0:
        ret += str(n%3)
        n = math.floor(n/3)
        print(n)
    
    for i in range(1, len(ret)+1):
        answer += int(ret[-i])*(3**(i-1))

    print(answer)
    return answer

solution(45)