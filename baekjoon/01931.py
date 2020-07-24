N = (int)(input())

conf = list()

for i in range(N):
    n = input().split(' ')
    start = (int)(n[0])
    end = (int)(n[1])
    conf.append([start, end])

# N = 11
# conf = [
#     (2,13), (12,14),
#     (1,4), (3,5), (0,6),
#     (6,10), (8,11), (8,12),
#     (5,7), (3,8), (5,9)
# ]


# 첫 정렬 기준은 1번째 컬럼으로, 두번째 정렬 기준은 0번째 컬럼으로
conf = sorted(conf, key=lambda x : (x[1], x[0]))
# print(conf)
cnt = 0
endTime = 0
for i in range(N):
    start_time = conf[i][0]
    finish_time = conf[i][1]

    if start_time >= endTime:
        endTime = conf[i][1]
        cnt+=1
        #print("{0} {1}".format(start_time, endTime))

print(cnt)

# 정렬한 후 겹치는 것을 삭제하고 다시 빠른 것을 찾아도되지만
# 시간이 오래걸림
# 회의를 하는 횟수가 중요한 것이므로
# 끝나는 시간만 보면 된다..

# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
# 이 부분은 함정이니.. 알고있는 것과 조금 다르게 적용해야함..