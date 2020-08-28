import sys
read = lambda : sys.stdin.readline().strip()

N = (int)(input())
tri = list()
for _ in range(N):
    a = [(int)(i) for i in read().split()]
    tri.append(a)
# print(tri)


# M(i, j) = i번째 줄의 j번째 원소를 골랐을때 최대합
# 양쪽 끝이 아닌 경우
# M(i, j) = max( M(i-1, j-1), M(i-1, j) ) + tri(i,j)
# 양쪽 끝인 경우
# M(i, 0) = M(i-1, 0) + tri(i,0)
# M(i, END) = M(i-1, END) + tri(i, END)

def M(i=0, j=0):
    global N
    cache = list()
    for _ in range(N):
        cache.append(list())
    cache[0].append(tri[0][0])

    for i in range(1, N):
        row_size = i+1

        for j in range(0,row_size):
            if j==0:
                cache[i].append(cache[i-1][0] + tri[i][j])
            elif j==row_size-1:
                cache[i].append(cache[i-1][row_size-2] + tri[i][j])
            else:
                cache[i].append(max(cache[i-1][j-1], cache[i-1][j]) + tri[i][j])

    return max(cache[N-1])

print(M())
        

