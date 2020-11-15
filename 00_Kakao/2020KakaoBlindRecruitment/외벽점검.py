'''
n은 1 이상 200 이하인 자연수입니다.
weak의 길이는 1 이상 15 이하입니다.
서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
weak의 원소는 0 이상 n - 1 이하인 정수입니다.
dist의 길이는 1 이상 8 이하입니다.
dist의 원소는 1 이상 100 이하인 자연수입니다.
친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.
'''

# 수가 작아서 전체 탐색 해도 될것같다.
# 어떤 친구를 먼저 투입할지도 모르니, 전체 탐색 해야할 것 같다.

import sys

# 원형 좌표를, 선형 좌표로 바꿔준다
def convert_linear(weak, idx, n):
    ret_clock = []

    for i in range(idx, idx + len(weak)):
        item = weak[i % len(weak)]
        if item < weak[idx]:
            item += n
        ret_clock.append(item)

    return ret_clock

# dist 배열의 모든 조합을 만들어 반환한다
tmp_list = []
visited = []
def all_list(aList, depth, ret):
    global tmp_list, visited
    if depth == len(aList):
        ret.append(tmp_list.copy())
        return

    for i in range(len(aList)):
        if not visited[i]:
            tmp_list.append(aList[i])
            visited[i] = True
            all_list(aList, depth + 1, ret)
            del tmp_list[-1]
            visited[i] = False

    return

def solution(n, weak, dist):
    answer = sys.maxsize

    # dist의 가능한 모든 조합 구하기
    global tmp_list, visited
    tmp_list = []
    visited = [False] * len(dist)
    dist_all = list()
    all_list(dist, 0, dist_all)


    for idx in range(len(weak)):
        # 각 취약지점을 시작으로 마지막 취약지점까지, 원형 좌표를 선형좌표로 바꾸기
        weak_linear = convert_linear(weak, idx, n)

        # 취약지점들을, 모든 조합으로 검사해보기
        for a_dist in dist_all:
            # 취약지점을 검사해보자
            weak_idx = 0
            weak_idx_tmp = 0
            dist_idx = 0
            # 투입할 친구가 남아있다면
            while dist_idx < len(a_dist):
                # 한 명이 취약지점에서 출발하여, 어디까지 커버하는가?
                one_start = weak_linear[weak_idx]
                one_end = one_start + a_dist[dist_idx]
                for k in range(weak_idx, len(weak_linear)):
                    # k 지점이 커버되는 곳이라면
                    if weak_linear[k] <= one_end:
                        weak_idx_tmp = k
                    else:
                        break

                # 새롭게 커버할 지점을 설정한다, 커버된 지역 다음 지역으로 설정
                weak_idx = weak_idx_tmp + 1
                if weak_idx >= len(weak_linear):        # 전부다 커버했다면
                    answer = min(answer, dist_idx + 1)  # 커버에 투입한 사람 수를 정답에 넣는다
                    break
                # 새로운 사람(다음 사람)을 설정한다
                dist_idx += 1

    # 모두 커버한 적이 없다면, -1을 반환한다
    if answer == sys.maxsize:
        return -1
    
    print('answer', answer)
    return answer


n = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]
solution(n, weak, dist)