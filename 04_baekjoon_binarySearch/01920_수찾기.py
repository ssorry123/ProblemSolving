class biTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, value):
        me = self
        
        while True:
            if me.value == value:
                # 이미 존재하므로 추가 불가
                break
            elif value < me.value:
                if me.left == None:
                    me.left = biTree(value)
                    break
                else:
                    me = me.left
            else:
                if me.right == None:
                    me.right = biTree(value)
                    break
                else:
                    me = me.right

    def find(self,value):
        me = self
        
        while True:
            if me.value == value:
                print(1)
                break
            elif value < me.value:
                if me.left == None:
                    print(0)
                    break
                else:
                    me = me.left
            else:
                if me.right == None:
                    print(0)
                    break
                else:
                    me = me.right      

N = (int)(input())

A = [(int)(i) for i in input().split()]
root = biTree(A[0])
for i in range(1,N):
    root.add(A[i])

M = (int)(input())

B = [(int)(i) for i in input().split()]
for i in B:
    root.find(i)

