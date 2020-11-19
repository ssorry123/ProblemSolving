def solution(strings, n):
    answer = []

    # n번째 문자로 정렬, n번째 문자가 같을 경우, 전체 사전 순으로 정렬
    answer = sorted(strings, key = lambda x : (x[n], x))

    return answer
    