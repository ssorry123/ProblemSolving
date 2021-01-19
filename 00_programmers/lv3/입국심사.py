# mid시간에 가능한가?
def check(mid, n, times):
    ret = 0
    # 각 심사관들이 mid 시간에 심사하는 사람 수 mid//t
    for t in times:
        ret += mid//t
    if ret>=n:
        return True
    else:
        return False
    
def solution(n, times):
    answer = 0
    # 모든 심사관들이 n명을 심사하는데 걸리는 최소시간
    low = 0
    # 모든 심사관들이 n명을 심사하는데 걸리는 최대 시간
    # 가장 심사시간이 오래걸리는 심사관 한명에게 모두 심사 받는 경우
    high = 1000000000*n
    
    # mid 가능할 경우 더 짧은 시간에도 가능한지 알아보기 위해 high=mid-1로 변경
    # mid 불가능할 경우 더 긴시간에 가능한지 알아보기 위해 low=mid+1로 변경
    # 가능한 시간의 lowbound를 찾는 문제이므로, 마지막에 low가 가리키게 됨
    while(low<=high):
        mid = (low+high)//2
        # mid시간에 가능하면 더 짧은 시간을 찾아본다
        if check(mid, n, times):
            high = mid - 1
        else:
            low = mid + 1
    answer = low
    
    
    return answer