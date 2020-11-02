import math
import heapq

def solution(arr):
    answer = 0

    # min heap
    heapq.heapify(arr)

    # 작은 두수를 뽑아서, 최소공배수로 만들고
    # 다시 heap에 집어넣는다
    while len(arr) >= 2:
        a, b = heapq.heappop(arr), heapq.heappop(arr)
        g = math.gcd(a, b)  # 최대공약수
        # make lcm 최소공배수 만들기
        lcm = g * int(a/g) * int(b/g)
        heapq.heappush(arr, lcm)

    answer = arr[0]
    print(answer)
    return answer

solution([3,2,1])