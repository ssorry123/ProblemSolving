# 부분트리

import sys
read = lambda : sys.stdin.readline().strip()

N, M = map(int, read().split())

arr = [0]
for _ in range(N):
    arr.append(int(read()))

segmentTree = [0]*(4*N) # (최소값, 최대값) 저장
# left, right는 arr에서 구간을 나타남[left, right]
# node는 segmentTree의 노드 번호
def makeSegmentTree(left, right, node):
    global segmentTree
    # 더이상 나눌 수 없는 경우
    if left==right:
        segmentTree[node] = (arr[left], arr[left])
        return segmentTree[node]

    # 구간 나누기
    mid = (left+right)//2
    lmin, lmax = makeSegmentTree(left, mid, node*2)
    rmin, rmax = makeSegmentTree(mid+1, right, node*2 + 1)

    nmin = min(lmin, rmin)  # 현재 구간의 최소값
    nmax = max(lmax, rmax)  # 현재 구간에 최대값
    segmentTree[node] = (nmin, nmax)
    return segmentTree[node]

# 세그먼트 트리 만들기
makeSegmentTree(1, N, 1)


# arr 범위 [left, right];;  node가 커버하는 arr의 범위
def search(left, right, node=1, nodeLeft=1, nodeRight=N):
    # 질의 구간[left,right]와 완전히 겹치는 경우
    if left <= nodeLeft and nodeRight <= right:
        return segmentTree[node]
    
    # 겹치는 구간이 없을 경우
    if nodeLeft > right or nodeRight < left:
        return (sys.maxsize, -sys.maxsize)
    
    # 구간 나누기
    mid = (nodeLeft+nodeRight)//2
    lmin, lmax = search(left, right, node*2, nodeLeft, mid)
    rmin, rmax = search(left, right, node*2+1, mid+1, nodeRight)

    return (min(lmin, rmin), max(lmax, rmax))

for _ in range(M):
    a, b = map(int, read().split())
    a, b = search(a,b)
    print(a, b)

