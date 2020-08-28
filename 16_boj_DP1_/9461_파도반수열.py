cache = [0] * 101
cache[1] = 1
cache[2] = 1
cache[3] = 1

# cache[n] = cache[n-2] + cache[n-3]

T = (int)(input())

for _ in range(T):
    N = (int)(input())
    if N <= 3:
        print(cache[N])
        continue

    for i in range(4, N+1):
        cache[i] = cache[i-2] + cache[i-3]
    print(cache[N])