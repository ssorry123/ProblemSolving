import sys

read = lambda : sys.stdin.readline().strip()

test_case = (int)(read())

class Ret:
	cache = [-1] * 41 # 0 <= n <= 40


def fibo(n):
	# 한 번 호출된 적이 있는 경우
	if Ret.cache[n] != -1:
		return Ret.cache[n][0], Ret.cache[n][1]
	# 직접적으로 0, 1을 호출 하는 경우
	elif n==0:
		return 1, 0
	elif n==1:
		return 0, 1

	# 어차피 한번은 끝까지 내려가야함
	a0, a1 = fibo(n-1)
	b0, b1 = fibo(n-2)
	Ret.cache[n] = [a0+b0, a1+b1]

	return a0+b0, a1+b1

for _ in range(test_case):
	n = (int)(read())
	ret = fibo(n)
	print("{0} {1} ".format(ret[0], ret[1]))