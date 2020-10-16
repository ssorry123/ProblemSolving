# 구명보트를 가장 적게 사용하자
# 그리디 문제라는데, 그리디를 적용했을때
# 최고의 해결방법이라는 것을 증명 또는 이해 또는 감으로 느낄 수 있는가..?

# 최대 두명밖에 탈 수 없고, 반드시 한명은 태울 수 있다
# 무거운 사람은 일단 태우고, 가장 가벼운 사람을 더 태울 수 있다면 태우자
def solution(people, limit):
    answer = 0  # 보트의 개수
    # 많은 무게부터 정렬
    people = sorted(people, reverse = True)
    left = 0
    right = len(people) - 1
    while left<=right:
        answer += 1 # 보트 추가
        onboat = people[left]
        left+=1
        # 남는 자리에 가벼운 사람을 태울 수 있다면
        if onboat + people[right] <= limit:
            right -= 1
    
    return answer