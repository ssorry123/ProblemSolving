# rocks에서 n개 바위를 제거한 후, 바위 사이의 거리 최소값의, 가능한 최대값
# 백준 이분탐색 공유기설치랑 비슷한 문제인듯

def solution(distance, rocks, n):
    answer = 0
    rocks.append(0)
    rocks.append(distance)
    rocks = sorted(rocks)
    n = len(rocks) - n  # 존재해야 하는 지점(시작, 도착 포함)
    
    left, right = 0, distance
    while left<=right:
        # mid = 각 지점 사이의 최소 거리
        mid = (left+right)//2
        
        # 최소거리 이상만큼 뛰어서 돌이 존재하는가?
        cnt = 1     # 시작지점 선택
        before = 0  # 시작지점 선택
        for i in range(1, len(rocks)):
            # 최소거리이상 차이가 난다면
            if rocks[i] - rocks[before] >= mid:
                before = i  # 선택
                cnt += 1

        # 선택한 지점들이 n개 이상 있다면, 최소 거리를 늘려봐도 된다
        if cnt>=n:
            left = mid + 1
        else:
            right = mid - 1
            
    return right