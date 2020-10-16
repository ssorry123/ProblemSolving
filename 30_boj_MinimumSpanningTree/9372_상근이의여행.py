# 각 간선의 가중치는 없다

# 무조건 read를 쓰자
import sys
read = lambda : sys.stdin.readline().strip()

def find(u, ds):
    if ds[u] == u:
        return u
    # 자신의 그룹 찾기
    ds[u] = find(ds[u], ds)
    return ds[u]

def union(u, v, ds):
    # 집합을 합칠때 항상 a가 b밑으로 들어가므로
    # 기준을 정해주어야 한다
    if u==v:
        return
    if u>v:
        tmp = u
        u=v
        v=tmp

    a, b = find(u, ds), find(v, ds)
    ds[a] = b   # a의 부모를 b로 하고
    return

def solution(n, m):
    # 각 국가 집합
    ds = list()
    for i in range(n+1):
        ds.append(i)
    
    # 비행기 노선 입력
    arr = list()
    for _ in range(m):
        a, b = map(int, read().split())
        arr.append((a,b))

    answer = 0
    # 간선의 가중치가 모두 1이므로 정렬해주지 않아도 됨
    for u, v in arr:
        a, b = find(u, ds), find(v, ds)
        # 싸이클을 만든다면 넘어감
        if a==b:
            continue

        # 비행기로 두 국가 연결
        union(u, v, ds)
        answer += 1

        # 모든 국가가 연결되었다면 출력후 종료
        c = find(ds[1], ds)
        cnt = 1
        for i in range(2, n+1):
            if find(ds[i], ds)!=c:
                break
            cnt+=1

        if cnt==n:
            print(answer)
            return
    

T = int(input())
for _ in range(T):
    n, m = map(int, read().split())
    solution(n, m)
    