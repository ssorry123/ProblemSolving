import sys
MAX = sys.maxsize
read = lambda : sys.stdin.readline().strip()

n = int(read())
m = int(read())

# 한 마을에서 다른 마을까지 최소 거리 저장
# 초기화
d = list()
for _ in range(n+1):
    d.append([MAX]*(n+1))

# 입력 받기
for _ in range(m):
    # a==b인 경우는 없다
    a, b, c = map(int, read().split())

    # a->b의 버스가 여러개 있으므로 해줘야 함
    # 가장 빠른 버스만 저장
    if c < d[a][b]:
        d[a][b] = c


# 플로이드 와샬 알고리즘
# i = 거쳐가는 노드
# a = 출발노드, b = 도착노드
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 출발지와 도착지가 같은 경우
            if a==b:
                continue
            
            # a->i->b가 가능하다면
            if d[a][i] != MAX and d[i][b] != MAX:
                d[a][b] = min(d[a][b], d[a][i]+d[i][b])


# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        out = d[i][j]
        if out == MAX or i==j:
            out = 0
        print(out, end=' ')
    print()
            