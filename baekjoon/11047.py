a = input()
N = (int)(a.split(' ')[0])
K = (int)(a.split(' ')[1])

coin = list()
[coin.append((int)(input())) for i in range(N)]
#print(coin)

# N = 10
# K = 4200
# coin = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]


cnt = 0
i=-1
while K>0:
    tmp = (int)(K / coin[i])

    # 가장 가치가 큰 동전으로 K를 채울 수 있으면
    if  tmp > 0:
        K -= tmp * coin[i]
        cnt += tmp

    elif tmp == 0:
        i -= 1

print(cnt)
