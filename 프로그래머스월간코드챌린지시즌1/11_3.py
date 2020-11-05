''' 대회 당시 AC '''
# Counter 알차게 써먹음
# 어려웠던 문제
from collections import Counter

'''
부분수열 조건
- len(x)는 짝수
- len(x) == 2n일 때
- {x[0], x[1]}, {x[2], x[3]}, ..., {x[2n-2], x[2n-1]}
- x[0] != x[1], x[2] != x[3], ..., x[2n-2] != x[2n-1]
'''

def check_star(val, arr):
    # val이 위치한 idx를 찾는다
    idx_list = [-1]
    for idx in range(len(arr)):
        if arr[idx] == val:
            idx_list.append(idx)
    idx_list.append(len(arr))


    # 각 idx 사이의 간격을 구한다
    interval = []
    for idx in range(1, len(idx_list)):
        interval.append(idx_list[idx] - idx_list[idx-1] - 1)


    # interval에 있는 것을 하나씩 가져가보자
    ret = 0
    for i in range(len(interval) - 1):
        # 일단 왼쪽에서 가져갈 수 있으면 가져간다
        if interval[i]>0:
            interval[i]-=1
            ret += 1
            
        # 왼쪽에서 가져갈 수 없으면, 오른쪽에서 가져간다
        elif interval[i+1]>0:
            interval[i+1]-=1
            ret += 1

        # 오른쪽에서도 가져갈 수 없으면
        # 포기하고 뒤로 가서 만들자
        else:
            pass

    return ret

def solution(a):
    answer = 0

    # 배열의 각 원소 개수를 센다
    d = list(Counter(a).items())
    # 배열의 원소가 많은 순으로 정렬한다
    d = sorted(d, key = lambda x:-x[-1])

    # 모든 집합은 최소 1개 이상 같아야 하므로
    # 겹치는 원소를 정하고, 부분수열을 만들어보자
    for val, cnt in d:
        # val을 겹치는 원소로 정하고 부분수열을 만들었을때
        # 나올수 있는 결과의 가능한 최대 값이 구해진 값보다 클 경우
        if cnt > answer:
            answer = max(answer, check_star(val, a))


    answer *= 2
    print(answer)
    return answer

solution([0,3,3,0,7,2,0,2,2,0])
solution([5,2,3,3,5,3])
solution([])