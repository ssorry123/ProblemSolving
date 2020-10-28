import sys
sys.setrecursionlimit(10**9)


answer = 0
def dfs(idx, sum, n, money):
    # print('sum', sum)
    if sum==n:
        global answer
        answer += 1
        return
    
    for next_idx in range(idx, len(money)):
        if sum + money[next_idx] > n:
            return
        dfs(next_idx, sum + money[next_idx], n, money)

def solution(n, money):
    
    '''
    ex) n==5, money = [1,2,5]인 경우

    '''

    # 일단 크기순으로 정렬
    money = sorted(money)

    global answer
    answer = 0
    dfs(0, 0, n, money)

    print(answer)

    return answer

