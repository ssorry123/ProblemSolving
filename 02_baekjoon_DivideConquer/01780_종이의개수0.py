'''
python3 시간 초과
pypy3 정답
실행 시간 : 5892ms
'''

class Matrix:
    minus = 0
    zero = 0
    plus = 0

    def __init__(self, matrix):
        self.matrix = matrix
        self.N = len(matrix)

    @classmethod
    def ret(cls):
        print(cls.minus)
        print(cls.zero)
        print(cls.plus)

    def check(self):
        mat = self.matrix
        N = self.N
        cnt_minus = 0
        cnt_zero = 0
        cnt_plus = 0

        # 나의 색종이가 모두 같은 색인지 확인
        for row in mat:
            cnt_minus += row.count(-1)
            cnt_zero += row.count(0)
            cnt_plus += row.count(1)
        
        # 모두 같은 색이면 갯수 증가 후 True리턴
        cnt = N*N
        if cnt == cnt_minus:
            Matrix.minus += 1
            return True
        elif cnt == cnt_zero:
            Matrix.zero += 1
            return True
        elif cnt == cnt_plus:
            Matrix.plus += 1
            return True
        else:
            return False


    def divide(self):
        N = self.N
        N13 = (int)(N/3) 
        N23 = (int)(2*N/3)
        # 자기 자신이 모두 같은 색인지 확인
        if self.check() == True:
            return

        # 모두 같은 색이 아니면 9등분 후 다시 확인
        Mats = [list() for i in range(9)]
        for i in range(N):
            row = self.matrix[i]
            if i<N13:
                Mats[0].append(row[0 : N13])
                Mats[1].append(row[N13 : N23])
                Mats[2].append(row[N23 : N])
            elif i<N23:
                Mats[3].append(row[0 : N13])
                Mats[4].append(row[N13 : N23])
                Mats[5].append(row[N23 : N])
            else:
                Mats[6].append(row[0 : N13])
                Mats[7].append(row[N13 : N23])
                Mats[8].append(row[N23 : N])

        for i in range(9):
            Matrix(Mats[i]).divide()

    def __str__(self):
        ret = '...\n'
        for row in self.matrix:
            ret += (str)(row)+'\n'
        ret += '...\n'
        return ret
    
# 입력 받기
N = (int)(input())
tmp = list()
for i in range(N):
    a = input().split(' ')
    a = [(int)(i) for i in a]
    tmp.append(a)


A = Matrix(tmp)
A.divide()
A.ret()