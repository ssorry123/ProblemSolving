# boj pypy3 통과
# python3 시간초과

import sys
read = lambda : sys.stdin.readline().strip().split()

class SgmtTree:
    """n 길이의 arr로 부분트리를 만든다"""
    def __init__(self, n, arr):
        self.sum = [0] * (4*n)  # 부분트리 배열
        self.n = n
        self.__make_tree(1, 0, self.n - 1, arr)
        return
    def __make_tree(self, idx, left, right, arr):
        """arr[left, right]의 합을 sum[idx]에(idx노드에) 저장,,, O(N)"""
        # 단말 노드 도착
        if left == right:
            self.sum[idx] = arr[left]
            return self.sum[idx]
        
        # 자신의 양쪽 자식 노드 구간합은 자신의 구간합
        mid = (int)((left + right)/2)
        temp1 = self.__make_tree(2*idx, left, mid, arr)
        temp2 = self.__make_tree(2*idx + 1, mid + 1, right, arr)
        self.sum[idx] = temp1 + temp2
        return self.sum[idx]
    
    def search_tree(self, left, right):
        """부분트리를 이용하여 left~right번째 원소들의 합을 구한다"""
        return self.__search_tree(1, 0, self.n - 1, left - 1, right - 1)
    def __search_tree(self, idx, arr_left, arr_right, left, right):
        """idx노드가 가진 [arr_left, arr_right]구간에서 [left, right]구간의 합을 구한다 O(lgN)"""
        # 구간이 우리가 원하는 구간에 포함될 경우 (교집합이 [arr_left, arr_right]인 경우)
        if left <= arr_left and arr_right <= right:
            return self.sum[idx]
        # 구간이 완전히 일치하지 않는 경우
        if right < arr_left or left > arr_right:
            return 0
        
        mid = (int)((arr_left + arr_right)/2)
        temp1 = self.__search_tree(2*idx, arr_left, mid, left, right)
        temp2 = self.__search_tree(2*idx + 1, mid + 1, arr_right, left, right)
        return temp1 + temp2
    
    def update_tree(self, b, c):
        """arr의 b번째 원소를 c로 바꿈"""
        self.__update_tree(1, 0, self.n - 1, b - 1, c)
        return
    def __update_tree(self, idx, left, right, b, c):
        """세그먼트트리의 단말노드를 바꾼 후 위로 갱신해감"""
        if left == right:
            self.sum[idx] = c
            return

        mid = (int)((left + right)/2)
        if b <= mid:
            self.__update_tree(2*idx, left, mid, b, c)
        else:
            self.__update_tree(2*idx + 1, mid + 1, right, b, c)

        # 값을 수정하고 올라왔다면 자신의 값도 갱신 
        self.sum[idx] = self.sum[2*idx] + self.sum[2*idx +1]
        return

tmp = read()
N = (int)(tmp[0])  # 수의 개수
M = (int)(tmp[1])  # 수의 변경 횟수
K = (int)(tmp[2])  # 구간의 합을 구하는 횟수
arr = list()
for _ in range(N):
    arr.append((int)(input()))

# sgmentTree객체 생성
sgmtTree = SgmtTree(N, arr)

for _ in range(M+K):
    tmp = [(int)(i) for i in read()]
    # 구간합을 구하는 경우
    if tmp[0] == 2:
        print(sgmtTree.search_tree(tmp[1], tmp[2]))
    # 갱신하는 경우
    elif tmp[0] == 1:
        sgmtTree.update_tree(tmp[1], tmp[2])
    else:
        print("입력데이터 오류")