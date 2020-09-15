import sys
read = lambda : sys.stdin.readline().strip()
# 입력, O(n)
tmp = read().split()
N, C = int(tmp[0]), int(tmp[1])
loc = list()
for _ in range(N):
    loc.append(int(read()))

# 정렬 O(nlogn), 각 집의 좌표에 맞게
loc = sorted(loc)
# print(loc)

# 가장 인접한 두 공유기 사이의 최대 거리
# 공유기를 설치할 수 있는 조합의 개수 = (N, C)
# N이 너무 크다
# 이분 탐색 사용

# 첫번째 집과 마지막 집 사이의 거리
# 이 값보다는 클 수 없다, 공유기가 두개라면, 이 값이 결과가 된다
size = loc[-1] - loc[0]

# 공유기를 설치, 각 공유기들의 거리가 min_distance이상으로 되게 설치하면
# 가장 가까운(인접한) 두 공유기의 거리는 min_distance이상이 된다
def make(min_distance):
    global N, C, loc
    
    installed = set()
    # start위치는 반드시 설치한다고 했을때
    # (최대한 많이 설치하려면, 첫 집을 빼면 안된다)
    cnt = 1
    before_idx = 0
    for idx in range(1, len(loc)):
        if loc[idx] - loc[before_idx] >= min_distance:
            cnt += 1
            before_idx = idx
        if cnt >= C:
            return True

    return False

def solution():
    global N, C, loc, size
    if C==2:
        return size

    left, right = 0, size
    # mid이상 거리를 벌려서 공유기 C개를 설치할 수 있는가?
    # 불가능 하다면, 최소 간격 거리를 줄여야 한다
    # 가능하다면, 최소 간격 거리를  더 벌려서 공유기를 설치해보자
    while left<=right:
        mid = (left+right)//2
        if make(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right

print(solution())