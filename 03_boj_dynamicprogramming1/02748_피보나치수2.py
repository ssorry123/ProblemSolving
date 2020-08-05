import sys

read = lambda : sys.stdin.readline().strip()

N = (int)(read())
# print(N)

# 1<= N <=90
cache = [-1]*91

def fibo(n):
    ret = cache[n]
    # base case
    if n==0 or n==1:
        return n
    elif ret != -1:
        return ret
    ret = cache[n] = fibo(n-1) + fibo(n-2)
    return ret
    
print(fibo(N))