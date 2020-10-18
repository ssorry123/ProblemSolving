import sys
read = lambda : sys.stdin.readline().strip()

# 입력
v, e = map(int, read().split())

weights = list()
for _ in range(e):
    a, b, w = map(int, read().split())
    weights.append((a,b,w))

weights = sorted(weights, key = lambda x : x[-1])

# 상호 배타 조합 세팅
def find(a, ds):
    if ds[a] == a:
        return a
    ds[a] = find(ds[a], ds)
    return ds[a]

def union(a, b, ds):
    a, b = find(a, ds), find(b, ds)
    if a==b:
        return
    if b>a:
        tmp = a
        a = b
        b = tmp
    ds[a] = b
    return

ds = list()
for i in range(v+1):
    ds.append(i)


# 최소 스패닝 트리
answer = 0
for a, b, w in weights:
    a, b = find(a, ds), find(b, ds)
    if a==b:
        continue
    
    union(a, b, ds)
    answer += w

print(answer)