K = (int)(input())

stack = list()


for _ in range(K):
    tmp = (int)(input())
    if tmp != 0:
        stack.append(tmp)       # 리스트 맨 뒤에 붙임
    else:
        stack.pop(len(stack)-1) # 리스트 맨 뒤 제거
    # print(stack)
print(sum(stack))
