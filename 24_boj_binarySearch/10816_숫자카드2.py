import sys
read = lambda : sys.stdin.readline().strip()
# 입력
N = map(int, read())
cache = dict()
# O(n)
for i in read().split() :
    if not i in cache:
        cache[i] = 1
    else:
        cache[i] += 1


M = map(int, read())
# O(n)
for i in read().split():
    if not i in cache:
        print(0, end = ' ')
    else:
        print(cache[i], end = ' ')

# 정렬하여 [O(nlogn)] 사용하는 이분탐색 보다는 빠르다..?