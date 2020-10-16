import sys
import math
read = lambda : sys.stdin.readline().strip()

n = int(read())

# 각 별의 좌표는 주어지는데,, 각 별사이의 거리는 주어지지 않는다
# 근데 최소 스패닝트리를 구해야함
# 거리를 구하고, 크루스칼 알고리즘을 쓰자

# 별좌표 입력받기
stars = list()
for _ in range(n):
    x, y = map(float, read().split())
    stars.append((x,y))

# 각 별 사이의거리 구하기
dist = list()
for i in range(n):
    for j in range(i+1,n):
        dx = math.pow(stars[i][0]-stars[j][0], 2)
        dy = math.pow(stars[i][1]-stars[j][1], 2)
        d = math.sqrt(dx+dy)
        dist.append((i,j,d))

# 각 별 사이 거리가 잛은 것부터 정렬
dist = sorted(dist, key = lambda x : x[-1])
# print(stars)
# print(dist)

# 유니온파인드 함수
def find(u, ds):
    if ds[u] == u:
        return u
    ds[u] = find(ds[u], ds)
    return ds[u]
def union(u, v, ds):
    # u>=v인 입력은 주어지지 않는다
    a, b = find(u, ds), find(v, ds)
    ds[a] = b
    return

# 답구하기
answer = 0
ds = list()
for i in range(n):
    ds.append(i)

for u, v, d in dist:
    a, b = find(u, ds), find(v, ds)
    # 싸이클을 만든다면
    if a==b:
        continue
    answer += d
    union(a, b, ds)

print(answer)

