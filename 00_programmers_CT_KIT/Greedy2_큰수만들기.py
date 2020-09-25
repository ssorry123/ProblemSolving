# 한 자연수(문자열)가 주어지고,
# 자연수에서 k개의 숫자를 제거할 수 있다
# (문자열의 길이 - k) 개의 숫자를 앞에서부터 순서대로 선택할 수 있다

# 문자열의 길이는 최대 백만, 모든 조합을 살펴 볼 순 없다

# 선택했을때, 가장 크게 만든 수는?
# 앞자리가 가장 커야함, 그리디

def solution(number, k):
    answer = ''
    str_len = len(number)
    ret_len = len(number) - k
    str_max = max(number)   # 존재하는 숫자 중 가장 큰 숫자를 찾음, O(n)

    
    # 앞에서 i번째 위치하게 되는 숫자를 찾는다
    # 0번째 숫자는, number의 뒤에서 5번째까지 숫자는 될 수 없다 [0,-5) 까지만 가능
    # 1번째 숫자는, number의 뒤에서 4번째까지 숫자는 될 수 없다 [choice+1, -4)
    choice = -1
    for i in range(ret_len, 0, -1):
        # 가능한 후보를 자름
        start = choice + 1
        end = str_len - i

        # 후보 중 가장 큰 값과 위치를 찾음 O(n)
        tmp, idx = -1, -1
        for will_idx in range(start, end+1):
            if int(number[will_idx]) > tmp:
                tmp = int(number[will_idx])
                idx = will_idx
            if int(number[will_idx]) == int(str_max):   # 시간 초과 방지 최적화
                tmp = int(str_max)
                idx = will_idx
                break

        # 가장 큰 값을 붙임
        answer+=number[idx]

        # 붙인 위치 이후부터 검사하도록 설정
        choice = idx
        
    return answer

solution('4177252841', 4)