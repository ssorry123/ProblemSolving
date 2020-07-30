import sys
N = (int)(input())

stair = list()
stair.append(0) # 0번째 계단, 계단에 포함되지 않음
for _ in range(N):
    stair.append((int)(input()))

# 마지막 계단에서 0번째 계단으로 내려가는 방법
# 마지막 계단은 이미 밟은 상태
# 어떤 계단에서든지 1만큼 두번 내려가면 연속된 3개의 계단을 밟게됨
# 단, 2번 계단에서 두번 내려가는 것은 제외
# 완전탐색 재귀법은 시간초과
def down(n, icnt=0):
    print(n)
    if n==0:
        return 0
    
    ret_1 = ret_2 = ret = 0

    # 1계단 내려갈 수 있는 경우
    if icnt==1 and n==1:    # 첫계단에서 1계단 또 내려갈 수 있는 유일한 경우
        ret_1 = stair[n] + down(n-1, 1)
    elif icnt!=1 and n-1>=0: # 1계단 내려온 것이 아니라면 1계단 내려가기 가능
        ret_1 = stair[n] + down(n-1, 1)
    
    # 2계단 내려갈 수 있는 경우
    if n-2>=0:
        ret_2 = stair[n] + down(n-2)
    
    ret = max(ret_1, ret_2)
        
    
    return ret

# 마지막 N번째 계단은 반드시 밟아야 한다
# 마지막 N번째 계단에 오는 방법은 1) N-1계단을 밟고 오는 경우
# 2) N-2계단을 밟고 오는 경우
# 1)의 경우 N-1, N을 밟게되므로 N-1을 밟기 전에는 반드시 N-3에서 출발하여야함
# 2)의 경우 2칸을 올라가는 것이므로 N-2를 밟기전에 1칸or2칸으로 올라왔던지 상관 없다
# M(N) = max ( M(N-3) + s[N-1] + s[N], M[n-2] + s[N] )
# 반복문 말고 재귀, 메모리제이션을 사용해서 구현해보자..
cache = list()
for _ in range(N+1):
    cache.append(-1)
def M(N):
    """int N >= 1"""
    global stair

    if N==1:
        return stair[1]
    elif N==2:
        return max(stair[2], stair[1] + stair[2])
    elif N==3:
        return max(stair[1] + stair[3], stair[2] + stair[3])

    if cache[N] != -1:
        return cache[N]
    
    
    ret_1 = M(N-3) + stair[N-1] + stair[N]
    ret_2 = M(N-2) + stair[N]
    ret = max(ret_1, ret_2)
    cache[N] = ret
    return ret


print(M(N))