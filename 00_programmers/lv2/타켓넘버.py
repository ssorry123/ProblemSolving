# 연산자의 개수는 numbers의 개수만큼
op = []
g_answer = 0
def cal(N, numbers):
    ret = numbers[0]
    if op[0] == '-':
        ret = -ret

    for i in range(1, N):
        if op[i]=='+':
            ret += numbers[i]
        elif op[i]=='-':
            ret -= numbers[i]
    return ret
def dfs(i, numbers, target):
    global op, g_answer
    if(i==len(numbers)):
        result =  cal(len(numbers), numbers)
        if result == target:
            g_answer += 1
        return
    op.append('+')
    dfs(i+1,numbers, target)
    op.pop(-1)
    op.append('-')
    dfs(i+1,numbers, target)
    op.pop(-1)
    
def solution(numbers, target):
    answer = 0
    dfs(0, numbers, target)
    answer = g_answer
    return answer