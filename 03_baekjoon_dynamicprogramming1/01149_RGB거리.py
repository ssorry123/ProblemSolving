import sys
read = lambda : sys.stdin.readline().strip()

R = 0
G = 1
B = 2

# 입력 부분
N = (int)(read())   # 2<=<=1000
cost2 = list()
for _ in range(N):
	a = [(int)(i) for i in read().split()]
	cost2.append(a)

# N이 1000이라면 색깔을 칠하는 경우의 수는 약 2^1000 = 10^100

# 반복문으로 구현 (점화식)

# D(i, color1) = min( D(i-1, color2), D(i-1, color3) ) + cost[i][color1]
# i번째 집까지 color1로 칠할때까지의 최소 비용은
# (i-1번째 집까지 color2, i-2번째 집까지 color3으로 색칠한 비용 중 최소비용) + (내집비용)
def D():
	global N
	cache = [ [0,0,0] for _ in range(N) ]
	cache[0] = [ cost2[0][R], cost2[0][G], cost2[0][B] ]
	
	for i in range(1, N):
		cache[i][R] = min(cache[i-1][G], cache[i-1][B]) + cost2[i][R]
		cache[i][G] = min(cache[i-1][R], cache[i-1][B]) + cost2[i][G]
		cache[i][B] = min(cache[i-1][R], cache[i-1][G]) + cost2[i][B]
		

	ret = cache[N-1]
	return min(ret[R], ret[G], ret[B])


print(D())

	