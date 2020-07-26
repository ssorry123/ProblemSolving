'''
python3 정답
pypy3 정답

종이의개수 0과 비교하여
-클래스 형식 버림
-input() 대신 readline() 사용
-check 함수 수정

종이의 개수 0과 비교에 이어 1과 비교하여
-재귀 부분에서 전달할 행렬을
 기존 행렬에서 복사하여 복사한 행렬을 재귀하지 않고
 입력받은 행렬은 복사되거나 하지 않고
 좌표와 크기를 이용하여 재귀호출함

pypy 실행 시간 : 2516ms
python 실행 시간 : 7712ms
'''

import sys
read = lambda : sys.stdin.readline().strip()

# 입력 받기
N = (int)(read())
mat = list()
for i in range(N):
	a = read().split()
	mat.append(a)


result = [0, 0, 0]
def check(start_row, start_col, size):
	N = size
	global result
	global mat

	# 나의 색종이가 모두 같은 색인지 확인
	# 시간 초과 나서 여기서 시간을 줄일 수 있지 않을까? 생각
	check_num = mat[start_row][start_col]	# 체크할 원소는 첫번째 원소를 기준

	# pypy3 정답, python3 시간초과
	for i in range(start_row, start_row + size):
		for j in range(start_col, start_col + size):
			if check_num != mat[i][j]:
				return False

	result[(int)(check_num) + 1] += 1
	return True


def divide(start_row, start_col, size):
	N = size
	N13 = (int)(N/3) 
	N23 = (int)(2*N/3)
	# 자기 자신이 모두 같은 색인지 확인
	if check(start_row, start_col, size) == True:
		return

	newSize = (int)(size/3)
	divide(start_row, start_col, newSize)
	divide(start_row + newSize, start_col, newSize)
	divide(start_row + newSize*2, start_col, newSize)

	divide(start_row, start_col + newSize , newSize)
	divide(start_row + newSize, start_col + newSize, newSize)
	divide(start_row + newSize*2, start_col + newSize, newSize)
	
	divide(start_row, start_col + newSize*2, newSize)
	divide(start_row + newSize, start_col + newSize *2, newSize)
	divide(start_row + newSize*2, start_col + newSize *2, newSize)



divide(0, 0, N)

for i in result:
	print(i)
