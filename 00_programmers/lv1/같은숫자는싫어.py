# 중복 된 원소 제거
# 순서 유지

def solution(arr):
    answer = [-1]

    for a in arr:
        # 연속되지 않는 다면 추가
        if a != answer[-1]:
            answer.append(a)


    return answer[1:]

