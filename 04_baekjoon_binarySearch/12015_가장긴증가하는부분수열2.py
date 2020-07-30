# 11053_가장긴증가하는부분수열과 같은 문제이지만
# 주어지는 수열 A의 길이가 1000->1000000
# 똑같이 재귀+메모라이제이션으로 풀면 시간 초과
import sys
read = lambda : sys.stdin.readline().strip()

"""
이진 탐색 카테고리에 있지만 해당 문제의 일부분을
해결하기위해 이진 탐색을 사용할 뿐
전체 문제 해결을 위한 아이디어 도출은 이진탐색과 무관하였다
이해가 잘 되지 않았지만 최대한 이해하려고 노력함
"""
"""
부분 증가수열의 최대길이가 궁금한 것이지
최대 길이의 부분 증가수열의 원소가 아니다
lower bound = 정렬된 배열에서 한 원소가 들어갈 수 있는 가장 작은 인덱스

주어진 배열 A의 원소를 순차적으로 이용해서 증가하는 수열을 만들어보자
1) 마지막 원소보다 넣으려는 값이 큰 경우 그냥 넣는다 ( 증가하는 수열의 길이 증가 )
2) 마지막 원소보다 작거나 같은 경우 lowerbound 위치랑 바꾼다
(증가하는 수열의 정렬된 상태는 깨지지 않으며 수열의 길이는 변하지 않는다)

"""
def lower_bound(A, value):
    """list A, int value, return index"""
    low = 0
    high = len(A) - 1
    mid = -1
    while low<=high:
        mid = (int)((low + high)/2)

        # mid가 value보다 크거나 같을 경우 mid를 줄여야 함
        # bound가 여러 개 있을때 가장 낮은 bound를 찾으려면
        # 조건에 맞았을때 내려가야함
        if A[mid] >= value:
            high = mid -1
        else:
            low = mid + 1

    # low가 가리키게 됨
    return low


N = (int)(read())
A = read().split()

ret = list()
ret.append((int)(A[0]))

# python3 가능
ret_last_index = 0
for i in range(1,N):
    a=(int)(A[i])
    if a > ret[ret_last_index]:
        ret.append(a)
        ret_last_index += 1
    else:
        ret[lower_bound(ret, a)] = a

# pypy3 가능, python3 시간 초과, max내장함수 수정
# for i in range(1,N):
#     a=(int)(A[i])
#     if a > max(ret):
#         ret.append(a)
#     else:
#         ret[lower_bound(ret, a)] = a

print(len(ret))

