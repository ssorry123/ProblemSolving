import sys
read = lambda : sys.stdin.readline().strip().split()

# 입력
N, M = map(int, read())
arr = list(map(int, read()))    # O(n)


'''
절단기 높이 H
H 증가 -> 가져갈 수 있는 나무의 길이 감소
H 감소 -> 가져갈 수 있는 나무의 길이 증가
최소 M미터의 나무를 가져갈때 H의 최대 길이를 찾아야함
H로 잘랐을때 최소 M미터 이상 나무를 가져갈 수 있으면 H 증가시켜보기(나무를 아끼자!)
최소 M미터 이상 가져갈 수 없다면 H를 감소시켜 가져가는 나무의 길이를 증가시킴
'''

# 작은 나무는 안잘릴수도 있으므로, 조건을 만족시키는지 확인할 때 큰나무들 부터 잘라본다
arr = sorted(arr, reverse = True)
def cut_tree(h):
    global arr
    cnt = 0
    for tree in arr:
        if tree > h:
            cnt = cnt + (tree - h)
        else:
            break
    
    if cnt >= M:
        return True
    else:
        return False

# 이분 탐색
# 0->모든 나무를 잘라서 가져감
# max -> 나무를 하나도 안가져감
left, right = 0, max(arr)   # O(n)
while left<=right:
    mid = (left+right)//2

    if cut_tree(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)
