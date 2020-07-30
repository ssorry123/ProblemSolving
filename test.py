import sys

# command1 = sys.stdin.readline().strip()
# command2 = sys.stdin.readline().split()
# print(command1)
# print(command2)
# #1234 123 41234 1234
# #['asdf', 'asdf', 'asdf', 'asdf']


# print([0]*9)
# # [0, 0, 0, 0, 0, 0, 0, 0, 0]

# a = 1

# def print_test():
#     print(a)
# print_test()

# 파이썬 참조하기
a = [-1]*10
print(a)
b = a
b[0] = 0
print(a)

print(-sys.maxsize)

print(10**7)

a = []
for _ in range(10):
    a.append([0, False])
print( a)
a[0][0] = 3
a[0][1] = True
print(a)

cache = [ [0,0,0] for _ in range(5) ]
print(cache)

# a = list()
# a[5]=3
# print(a)

cache = [-1] * (10)
print(cache)
cache[5] = 9999
print(cache)

cache = [[-1, 1]] * (10)
print(cache)
cache[5][0] = 9999
print(cache)

a = list()
max(a)