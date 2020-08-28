import sys

class Queue:
    def __init__(self):
        self.arr = list()
        self.pop_idx = 0
        return
    def garbageCollection(self):
        del self.arr[:self.pop_idx]
        self.pop_idx = 0
        return
    def size(self):
        return len(self.arr) - self.pop_idx
    def empty(self):
        if self.size() == 0:
            return 1
        return 0
    def push(self, X):
        self.arr.append(X)
        return
    def front(self):
        if self.empty() == 1:
            return -1
        return self.arr[self.pop_idx]
    def back(self):
        if self.empty() == 1:
            return -1
        return self.arr[-1]
    def pop(self):
        if self.empty() == 1:
            return -1
        ret = self.arr[self.pop_idx]
        self.pop_idx += 1
        # 안해도 정답은 나옴
        if(self.pop_idx > 30000):
            self.garbageCollection()
        return ret

N = (int)(input())
q = Queue()
for _ in range(N):
    tmp = sys.stdin.readline().strip().split()
    op = tmp[0]
    if op == 'push':
        q.push((int)(tmp[1]))
    elif op == 'pop':
        print(q.pop())
    elif op == 'size':
        print(q.size())
    elif op == 'empty':
        print(q.empty())
    elif op == 'front':
        print(q.front())
    elif op == 'back':
        print(q.back())
    else:
        pass

