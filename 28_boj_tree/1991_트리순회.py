import sys
read = lambda : sys.stdin.readline().strip()

N = int(read()) # 2진트리의 노드 개수

### make bi tree
Tree = dict()
class Node:
    Tree = dict()
    def __init__(self, ch, l, r):
        self.ch = ch
        self.left = l
        self.right = r
        
        global Tree
        Tree[ch] = self

for _ in range(N):
    me, left, right = read().split()
    Node(me, left, right)

# make method
def preorder(here = 'A'):    # MLR
    me = Tree[here]

    print(here, end = '')   # M
    if me.left != '.':      # L
        preorder(me.left)
    if me.right != '.':     # R
        preorder(me.right)

    return

def inorder(here = 'A'):    # LMR
    me = Tree[here]
    
    if me.left != '.':      # L
        inorder(me.left)
    print(here, end = '')   # M
    if me.right != '.':     # R
        inorder(me.right)

    return

def postorder(here = 'A'):  # LRM
    me = Tree[here]
    
    if me.left != '.':      # L
        postorder(me.left)
    if me.right != '.':     # R
        postorder(me.right)
    print(here, end = '')   # M

    return


preorder()
print()
inorder()
print()
postorder()
