import queue

cache = dict()
def dist(a, b, Graph, n):
    # a를 항상 작게
    if a>b:
        tmp = a
        a = b
        b = tmp
    
    # 이미 구한 거리가 있다면
    if (a,b) in cache:
        return cache[(a, b)]

    # BFS로 거리 구함
    q = queue.Queue()
    q.put((a,0))

    visited = [False] * (n+1)
    visited[a] = True
    while not q.empty():
        me, dist = q.get()
        if me==b:
            cache[(a,b)] = dist
            return dist
        
        for i in Graph[me]:
            if visited[i] == False:
                visited[i] = True
                q.put((i, dist+1))

                na, ni = a, i
                if na > ni:
                    tmp = na
                    na = ni
                    ni = tmp
                cache[(na, ni)] = dist+1

    return -1


def solution(n, edges):
    answer = 0
    # 트리이므로, 반드시 한 점에서 한점까지 경로는 존재하고,
    # 거리는 정해져있다
    # 플로이드와샬로, 한번 거리를 구했으면, 다시 안구해도 되지 않을까?
    # 그런데 n이 너무 크다,,, 모든 거리를 저장하고 있기에는 너무크다,
    # a,b,c간의 거리를 일단 구하고, 그다음부턴 캐시를 이용하는게
    # 내지식에선 최선의 방법인듯,,

    G = dict()
    for u, v in edges:
        if not u in G:
            G[u] = list()
        if not v in G:
            G[v] = list()
        
        G[u].append(v)
        G[v].append(u)

    global cache
    cache = dict()  # 캐시 초기화
    for a in range(1,n+1):
        for b in range(a+1, n+1):
            d1 = dist(a, b, G, n)
            for c in range(b+1, n+1):
                d2, d3 = dist(b, c, G, n), dist(a, c, G, n)
                arr = sorted([d1, d2, d3])
                answer = max(answer, arr[1])


    print(answer)
    return answer


print((250000**2)/2)
solution(4,[[1,2],[2,3],[3,4]])