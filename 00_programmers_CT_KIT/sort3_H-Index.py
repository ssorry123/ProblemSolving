def solution(citations):
    answer = 0
    
    low = 0
    high = len(citations)
    
    while low<=high:
        mid = (low+high)//2
        
        # h번 이상 인용된 논문 개수
        cnt = 0
        for c in citations:
            if c>=mid:
                cnt+=1
        
        if cnt>=mid:
            low = mid + 1
        else:
            high = mid - 1
    
    return high