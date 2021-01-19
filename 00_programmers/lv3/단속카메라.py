# 코드는 짧은데 생각하기 어려우면 현타옴

def solution(routes):
    answer = 1  # 일단 카메라는 한개는 있다
    # 진입 시점 정렬
    routes = sorted(routes, key = lambda x : x[0])
    
    a, b = routes[0]
    for j in range(1, len(routes)):
        print(a, b)
        c, d = routes[j]
        # 만약 [a,b] 와  [c,d] 가 겹치지 않는다면
        if b<c:
            answer += 1 # 카메라 추가
            a, b = c, d
            continue
        # 공통된 경로를 많이 찾을 수록 범위는 좁아지므로
        # 범위를 좁힌다
        a, b = c, min(b, d)
    
    return answer