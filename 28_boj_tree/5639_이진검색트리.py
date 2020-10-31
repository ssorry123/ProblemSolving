import sys
sys.setrecursionlimit(10**9)
readint = lambda : int(sys.stdin.readline().strip())

arr = list()

try:
    while True:
        arr.append(readint())
except:
    pass


# 배열 자체가 트리다
# 배열은 MLR로 되어있다 (preorder)
#   M          L                R
# (root) (left_sub ... ) ( right_sub ... )
# left_sub : root보다 작은 값들
# right_sub : root보다 큰 값들

# LRM
def postorder(left, right):
    root = arr[left]
    # 자식이 0인 경우
    if left == right:
        print(root)
        return
    
    # left_root
    left_root = left + 1

    # find right_root
    right_root = -1

    for i in range(left+1, right+1):
        if arr[i] > root:
            right_root = i
            break
    

    # 왼쪽 서브트리만 있는 경우
    if right_root == -1:
        postorder(left_root, right)
    # 오른쪽 서브트리만 있는 경우
    elif left+1 == right_root:
        postorder(right_root, right)
    # 둘다 있는 경우
    else:
        postorder(left_root, right_root-1)
        postorder(right_root, right)

    print(root)

postorder(0, len(arr)-1)

