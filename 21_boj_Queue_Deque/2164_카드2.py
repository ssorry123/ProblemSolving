# N=1인 경우 조심

N = (int)(input())

arr = [i for i in range(1,N+1)]
# print(arr)
start_idx = 0
end_idx = len(arr)-1

# 버릴 것이 있는 경우
while start_idx < end_idx:
    # 하나 버림
    start_idx += 1
    # 하나 남았다면
    if end_idx == start_idx:
        break
    # 하나를 맨 뒤로 옮김
    arr.append(arr[start_idx])
    start_idx += 1
    end_idx += 1

print(arr[start_idx])