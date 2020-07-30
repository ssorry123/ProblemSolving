I = input().split()
K = (int)(I[0])
N = (int)(I[1])
a = list()
for _ in range(K):
	a.append((int)(input()))
a.sort()

# K개의 랜선들을 크기에 따라 정렬한다
# low를 1, high를 가장 큰값으로 놓는다, 그 중간을 mid라고 한다
# 모든 랜선들을 mid만큼 잘랐을때 개수가 N이 안된다면 자르는 크기를 줄여야 한다 (high감소)
# 모든 랜선들을 mid만큼 잘랐을때 개수가 N보다 크거나 같다면 
""" 더 길게 잘라봐도 된다 (low증가) """

# 정답이 하나만 존재하는 평범한 2진탐색과는 조금 다르다
# 1부터 자를 수 있는 최대길이까지가 S라 할때, 자를 수 있는 길이들은
# 1,2,3,....., S-1, S, x, x, x, .... , max(a) -> S아래는 다 가능한 부분
# 결국 마지막에 low=high=S+1인 상태가 온다.(증명가능?..?)

low = 1
high = max(a)
mid = -1

# 탐색할 원소가 남아있는 경우
while low <= high:
	mid = (int)((low+high) / 2)

	cnt = 0
	for i in a:
		if i >= mid:
			cnt += (int)(i/mid)
	
	# 자연스럽게 가장 큰 길이를 고르게 됨
	# 맞는 것이 여러개 있을때 올라가는 경우
	# 가장 위에 있는 인덱스를 반환
	if cnt >= N:
		low = mid + 1
	else:
		high = mid - 1

# 마지막에 high가 가리키는 것이 가장 큰 길이
print(high)