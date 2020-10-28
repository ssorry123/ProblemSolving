# 문제 : (works의 원소)^2 의 합이 최소가 되도록 하는 문제인데,,
# works에서 최대값이 가장 작도록 하면 되는 문제이다,,

# 문제는, 최대값이 가장 작을때, 각원소의 제곱의 합이 가장 최소가 되느냐를
# 수학적으로 증명할 수 있느냐,,

# import queue
import heapq


def solution(n, works):
    answer = 0

    # lowest first  queue이므로, max heap으로 바꾸기 위해서
    # 음수로 저장한 다음 넣어준다
    for i in range(len(works)):
        works[i] = -works[i]
    heapq.heapify(works)

    # n번만큼 1 빼고 넣어준다
    for _ in range(n):
        val = -heapq.heappop(works)
        if val == 0:
            break
        heapq.heappush(works, -(val-1))

    # 야근지수를 구한다
    for val in works:
        answer += (val*val)

    return answer