import sys
read = lambda : sys.stdin.readline().strip().split()

class DisjointSet:
    ran = True
    def __init__(self, n):
        self.prt = [(int)(i) for i in range(n)]
    
    def found(self, a):
        """a가 속해있는 집합의 대표 idx 반환"""
        # 자신이 최상위 노드이면
        if self.prt[a] == a:
            return a
        
        # 최적화: 루트까지 만난 노드들 모두 부모를 루트로 설정
        self.prt[a] = self.found(self.prt[a])
        return self.prt[a]
    
    def merge(self, a, b):
        """a가 포함된 집합과 b가 포함된 집합 합치기"""
        aSet = self.found(a)
        bSet = self.found(b)
        if aSet == bSet:
            return
        
        ran = DisjointSet.ran
        if ran:
            self.prt[aSet] = bSet
        else:
            self.prt[bSet] = aSet
        DisjointSet.ran = not ran
        return

N = (int)(input())
M = (int)(input())
trip = DisjointSet(N)

# 연결된 도시 같은 집합으로 만들기
for i in range(N):
    tmp = read()
    # 대칭이므로 대각선으로 나눠서 절반만 검사
    for j in range(i):
        if(tmp[j] == '1'):
            trip.merge(i, j)

plan = read()   # 여행 계획
ret = True      # 처음부터 끝까지 같은 집합에 속해있다면
for i in range(len(plan) - 1):
    a = (int)(plan[i]) - 1
    b = (int)(plan[i+1]) - 1
    if trip.found(a) != trip.found(b):
        ret = False
        break

if ret:
    print('YES')
else:
    print('NO')
