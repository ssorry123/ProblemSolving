# 모든 행렬은 Matrix객체로 포함되며
# 실제 행렬은 Matrix객체의 멤버(2차원 리스트)
# 곱셈, 제곱은 모두 객체를 반환하도록 통일
class Matrix:
    """ Matrix(2차원 리스트) """
    def __init__(self, matrix):

        self.matrix = matrix

    # 자기 자신 행렬과 받은 행렬 곱하기 실행
    def times(self, other_matrix):
        A = self.matrix
        B = other_matrix.matrix
        lenA = len(A)
        lenB = len(B)
        if lenA != lenB:
            return "fatal"
        
        # (tmp1 + ... + tmpN)%1000 = (tmp1%1000 + ... +tmpN%1000)%1000
        ret = list()
        for i in range(N):
            ret.append(list())
            for j in range(N):
                tmp = 0
                for k in range(N):
                    a = A[i][k] # <=1000
                    b = B[k][j] # <=1000
                    tmp = (tmp + (a*b))%1000
                ret[i].append((int)(tmp))
        RetMatrix = Matrix(ret)   # 결과 객체 생성 후 객체 반환
        return RetMatrix
    
    
    # 출력 부분에 쓰레기같은 함정이있다..
    # 문제의 조건 -> [행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.]
    # pow(A,1) 같은 경우는 아무런 연산을 하지 않고 그대로 출력되게 된다.
    # 연산 부분에서 열심히 모듈러 연산을 해주어도 pow(A,1) 의 경우는 모듈러 연산이 적용되지 않기 때문에
    # 결과를 %1000으로 출력하라는 문제의 조건에 맞지 않게 된다..
    def __str__(self):
        ret = ''
        n  = len(self.matrix)

        for i in range(n):
            for j in range(n):
                ret += (str)(self.matrix[i][j] % 1000)+' '
            ret += '\n'

        return ret

# 재귀 함수
def pow(a_Matrix, b):
    """
    pow(Matrix matrix, int b)
    """
    # A(1), 기저사례1
    if b==1:
        return a_Matrix
    # A(2), 기저사례2, 없어도 됨
    elif b==2:
        return a_Matrix.times(a_Matrix)

    # A(N) = A(N/2) * A(N/2)
    elif b%2 == 0:
        half = pow(a_Matrix, (int)(b/2))
        return half.times(half)
    
    # A(N) = A(N-1) * A
    elif b%2 == 1:
        b_1 = pow(a_Matrix, (int)(b-1))
        return b_1.times(a_Matrix)

    """
    # 이론상 맞지만 한번의 리턴에 두번의 pow를 재귀호출 하므로 시간이 오래걸리게 된다
    # 잘못된 코딩..  분할 정복의 재귀호출은 보다 더 개념적으로,,
    # 한 함수가 결과를 리턴한다 생각하고 만들어야 한다
    # A(N) = A(N/2) * A(N/2)
    elif b%2 == 0:
        return pow(a_Matrix, (int)(b/2)).times(pow(a_Matrix, (int)(b/2)))

    # 홀수를 억지로 절반으로 나누면 효율이 아주 떨어지게 된다
    # A(N) = A(N/2-1) * A(N/2-1) * A(1)
    elif b%2 == 1:
        b -= 1
        return pow(a_Matrix, (int)(b/2)).times(pow(a_Matrix, (int)(b/2))).times(a_Matrix)
    """
    return False


# N, B 입력 받기
a = input().split(' ')
N, B = [(int)(i) for i in a]
# print("{0} {1}".format(N, B))

# N*N 행렬 A 입력받기
tmp = list()
for i in range(N):
    a = input().split(' ')
    a = [(int)(i) for i in a]
    tmp.append(a)
# 입력받는 A 행렬 생성
A = Matrix(tmp)

# 함수 실행
print(pow(A, B))