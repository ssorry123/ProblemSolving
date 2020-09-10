# AC
# numbers배열로, 가능한 모든 두 수의 조합을 만들어, 모든 조합의 합을 반환
def dfs(start, numbers, cnt = 0,sum = 0, ret = list()):
    if cnt == 2:
        if not sum in ret:
            ret.append(sum)
        return

    for i in range(start, len(numbers)):
        dfs(i+1, numbers, cnt + 1, sum + numbers[i], ret)
    
def solution(numbers):
    answer = []
    ret = dfs(0, numbers, 0, 0, answer)
    answer = sorted(answer) # 정렬하여 반환
    return answer