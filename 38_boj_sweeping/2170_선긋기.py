import sys
read = lambda : sys.stdin.readline().strip()

N = int(read())

arr = list()
for _ in range(N):
    arr.append(tuple(map(int,read().split())))

# 왼쪽부터 살펴보자
arr = sorted(arr)

answer = 0
left = right = None
for l, r in arr:
    if left == None:
        left = l
        right = r
        continue

    # 새로운 구간이 지금 구하고 있는 구간과 겹친다면
    # 구간을 합쳐주자
    if l<=right:
        right = max(right, r)
    # 겹치지 않는다면 새로운 구간 만들기
    else:
        answer += (right - left)    # 지금까지 구한 구간을 답에 추가하고
        left, right = l, r          # 새로운 구간 만들기

# 마지막 결과 반영
answer += (right - left)

print(answer)
