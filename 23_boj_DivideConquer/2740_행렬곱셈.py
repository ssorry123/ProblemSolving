a = input().split(' ')
N = (int)(a[0])
M = (int)(a[1])
A = list()
for i in range(N):
    tmp = input().split(' ')
    tmp = [(int)(i) for i in tmp]
    A.append(tmp)


a = input().split(' ')
M = (int)(a[0])
K = (int)(a[1])
B = list()
for i in range(M):
    tmp = input().split(' ')
    tmp = [(int)(i) for i in tmp]
    B.append(tmp)

# print('')
# print(A)
# print(B)

# 결과 행렬
# NM * MK = NK

C = list()
for i in range(N):
    C.append(list())


# [A row 0]의 원소들과
for n in range(N):
    # [B col 1]의 원소들이
    for k in range(K):
        tmp = 0
        # range(M) 횟수만큼 서로 곱한다
        for m in range(M):
            tmp += A[n][m] * B[m][k]
        C[n].append(tmp)


# 출력
for n in range(N):
    for k in range(K):
        print(C[n][k], end=' ')
    print('')

'''
이 문제의 쓰레기 같은 함정은 출력 부분에 있다.
문제에 "행렬의 각 원소는 공백으로 구분한다."
예제 정답을 음영으로 보면 (공백은 ㅁ로 표시)
-1ㅁ-2ㅁ6ㅁ
-3ㅁ-6ㅁ12ㅁ
-5ㅁ-10ㅁ18ㅁ
한 행의 마지막 원소 뒤에도 공백을 추가해주어야 한다
'''