N = (int)(input())

a = input().split(' ')
P = list()
[P.append((int)(i)) for i in a]
P = sorted(P)   # 오름차순 정렬
#print(P)

ret = 0
k = len(P)
for i in P:
    ret += (int)(i)*k
    #print(ret)
    k-=1
print(ret)

# 먼저 시작하는 음식들은 나중에 시작하는 음식들보다
# 많은 사람들의 기다리는 시간에 포함되므로
# 먼저 시작하는 음식의 조리시간이 가장 짧아야 된다고 생각