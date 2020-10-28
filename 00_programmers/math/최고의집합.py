'''
    n:2, s:9인경우
    {1,8}:8, {2,7}:14, {3,6}:18, {4,5}:20
    
    n:3, s:9인경우
    {3,3,3}:27로 제일 크다

    각 원소들의 차이가 가장 작을때, 
    각 원소들의 곱이 가장 크다는데

    느낌상으론 알겠는데, 수학적 증명을 해야 확실하게 이해할듯
'''

import math
def solution(n, s):
    answer = []
    # 1이 n개 있어도 s보다 크다면, 합이 s가 될 수 없다
    if 1*n > s:
        return [-1]

    # 각 원소의 기본 값
    mid = math.floor(s/n)

    # 모든 원소가 다 같아서, 차이가 모두 0이라면
    if s%n==0:
        return [mid]*n
    
    answer = [mid] * (n - s%n)
    answer += [mid+1] * (s%n)

    return answer