import sys
read = lambda : sys.stdin.readline().strip().split()

class DisjointSet:
    ran = True
    def __init__(self, n):
        self.prt = [(int)(i) for i in range(n)]
        self.sum = [1] * n  # 각 집합의 개수 저장
    
    def found(self, a):
        """a가 속해있는 집합의 대표 idx 반환"""
        # 자신이 최상위 노드이면
        if self.prt[a] == a:
            return a
        # 최적화: 루트까지 만난 모든 노드들의 부모를 루트로 설정
        self.prt[a] = self.found(self.prt[a])
        return self.prt[a]
    
    def merge(self, a, b):
        """a가 포함된 집합과 b가 포함된 집합 합치기, 합친후 원소 개수 반환"""
        aSet = self.found(a)
        bSet = self.found(b)
        if aSet == bSet:
            # 집합의 원소 개수 반환
            return self.sum[aSet] 
        
        # a집합과 b집합은 상호배타조합
        # 두 집합을 합집합하였을때 원소의 수는 그냥 더하면된다
        ran = DisjointSet.ran
        ret = 0
        if ran:
            self.prt[aSet] = bSet
            self.sum[bSet] += self.sum[aSet]
            ret = self.sum[bSet]
        else:
            self.prt[bSet] = aSet
            self.sum[aSet] += self.sum[bSet]
            ret = self.sum[aSet]
        DisjointSet.ran = not ran
        return ret
        

T = (int)(input())
for _1 in range(T):
    F = (int)(input())
    frdNet = DisjointSet(2*F)   # 네트워크에 가능한 최대 인원 = 2*F
    idx = 0
    name_dict = dict()          # key=이름, value=번호
    for _2 in range(F):
        tmp = read()
        a = b = 0
        # 입력된 이름들이 처음인지 아닌지
        if tmp[0] in name_dict:
            a = name_dict.get(tmp[0])
        else:
            name_dict[tmp[0]] = a = idx
            idx += 1
        if tmp[1] in name_dict:
            b = name_dict.get(tmp[1])
        else:
            name_dict[tmp[1]] = b = idx
            idx += 1

        # a친구들과 b친구들을 합침
        # print('anser :: ',frdNet.merge(a, b))
        print(frdNet.merge(a, b))