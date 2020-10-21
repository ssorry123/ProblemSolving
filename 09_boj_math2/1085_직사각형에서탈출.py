arr = [(int)(i) for i in input().split()]

ret = min(arr[0], arr[1])
ret = min(arr[2]-arr[0], ret)
ret = min(arr[3]-arr[1], ret)

print(ret)