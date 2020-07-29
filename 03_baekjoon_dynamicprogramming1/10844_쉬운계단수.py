N = (int)(input())

#         시작점
# X 1 2 3 4 5 6 7 8 9 , N=1
# 0 1 2 3 4 5 6 7 8 9 , N=2
# 0 1 2 3 4 5 6 7 8 9 , N=3
# ....
# 각 숫자들은 대각선으로만 이동할 수 있다
# 한 숫자에 도착하는 경우의 수는
# 자신의 대각선 위 양쪽 숫자까지 도착하는 경우의 수를 더한 것.
# ex : (3,6)까지 오는 경우의 수=(2,5)까지 오는 경우의 수 + (2,7)까지 오는 경우의 수

cache = list()
for _ in range(N+1):
    cache.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# 1번째, 0자리에서 한자리 숫자로 갈 수 있는 경우의 수
cache[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# cache[1] 을 이용해서 cache[2]를 만든다
for i in range(1, N):
    for j in range(0,9):
        cache[i+1][j+1] = cache[i][j]
    for j in range(1,10):
        cache[i+1][j-1] = cache[i+1][j-1] + cache[i][j]

ret = 0
for i in cache[N]:
    ret =  (ret + i) % 1000000000
    # ret += i % 1000000000   # 안됨
ret = ret % 1000000000  # 이건 안해도 답 나옴
print(ret)