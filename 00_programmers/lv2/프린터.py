def solution(priorities, location):
    answer = 0

    cnt = 0
    while len(priorities) > 0:
        top = max(priorities)
        # 출력할 문서가 가장 높은 우선순위이면
        if top == priorities[0]:
            del priorities[0]
            cnt += 1

            # 내가 원하는 문서였다면
            if location==0:
                return cnt
            # 내가 원하는 문서가 아니었다면
            else:
                location -= 1
        # 출력할 문서가 가장 높은 우선순위가 아니라면
        else:
            # 뒤로 보낸다
            priorities.append(priorities[0])
            del priorities[0]

            # 뒤로 보내진게 내가 원하는 문서였다면
            if location==0:
                location = len(priorities) - 1
            else:
                location -= 1
    
    return answer