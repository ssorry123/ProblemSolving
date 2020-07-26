'''
python3 시간 초과
pypy3 정답

종이의개수 0과 비교하여
-클래스 형식 버림
-input() 대신 readline() 사용
-string -> int 변환 안함
-check 함수 수정

실행 시간 : 5892ms -> 2212ms
'''

import sys
read = lambda : sys.stdin.readline().strip()

result = [0, 0, 0]

def check(mat):
	N = len(mat)
	global result

	# 나의 색종이가 모두 같은 색인지 확인
	# 시간 초과 나서 여기서 시간을 줄일 수 있지 않을까? 생각
	check_num = mat[0][0]	# 체크할 원소는 첫번째 원소를 기준

	# pypy3 정답, python3 시간초과
	for i in range(N):
		for j in range(N):
			if check_num != mat[i][j]:
				return False

	result[(int)(check_num) + 1] += 1
	return True


def divide(matrix):
	N = len(matrix)
	N13 = (int)(N/3) 
	N23 = (int)(2*N/3)
	# 자기 자신이 모두 같은 색인지 확인
	if check(matrix) == True:
		return

	# 모두 같은 색이 아니면 9등분 후 다시 확인
	Mats = [list() for i in range(9)]
	for i in range(N):
		row = matrix[i]
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
		divide(Mats[i])


	
# 입력 받기
N = (int)(read())
tmp = list()
for i in range(N):
	a = read().split()
	tmp.append(a)

divide(tmp)


for i in result:
	print(i)