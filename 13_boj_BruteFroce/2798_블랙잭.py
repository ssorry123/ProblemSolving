tmp = input().split()
N = (int)(tmp[0])
M = (int)(tmp[1])
arr = [(int)(i) for i in input().split()]

cur_max = 0
for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1, N):
            tmp = arr[a] + arr[b] + arr[c]
            if tmp <= M and cur_max < tmp:
                cur_max = tmp

print(cur_max)