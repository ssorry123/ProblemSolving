import sys
read = lambda : sys.stdin.readline().strip()

# 정방향의 사람인 경우는 신경쓰지 않아도 된다
# 어차피 0~M까지 가기 때문이다

# 역방향의 사람이 중요하다
# 왔던 길을 되돌아가는 일은 한번이면 충분하다
# 왔던길을 되돌아갔다가 다시 되돌아가는 짓을 하지 말자

N, M = map(int, read().split())

reverse1 = list()
for _ in range(N):
    a, b = map(int, read().split())
    # 역방향만 기억하자
    if a > b:
        reverse1.append((b, a))
reverse1 = sorted(reverse1, key=lambda x:x[0])


def solution(reverse):
    answer = M
    
    left = right = None
    for a, b in reverse:
        if left==None:
            left, right = a, b
            continue
        
        if right < a:
            # 지금까지 구간 저장하고, 새로운 구간 조사하러 가자
            answer = answer + 2*(right-left)
            left, right = a, b
        else:
            right = max(right, b)
    
    # 역방향이 없었던 경우에는, 그냥 M이 최소임
    if left == None:
        return answer

    # 마지막 구간 저장하고 반환
    answer = answer + 2*(right-left)
    return answer

print(solution(reverse1))