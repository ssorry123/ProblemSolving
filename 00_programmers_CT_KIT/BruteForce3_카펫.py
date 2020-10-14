def solution(brown, yellow):
    answer = []
    
    # rowC <= colC
    MAX = brown + yellow
    
    # 두 방정식의 조건을 만족하는 (rowC, colC) 쌍은 일대일 대응임
    # 2*rowC + 2*colC == brown + 4
    # rowC*colC = brown + yellow
    for rowC in range(3, MAX+1):
        if MAX % rowC != 0:
            continue
        colC = int(MAX/rowC)
        if 2*rowC + 2*colC == brown+4:
            return [colC, rowC]
        
    return answer