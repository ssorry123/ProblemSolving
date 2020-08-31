def solution(array, commands):
    answer = []
    # commands 반복
    for i, c in enumerate(commands):
        # 배열 자르기
        tmp = array[c[0] - 1 : c[1]]
        # 정렬
        tmp = sorted(tmp)
        # 정답 리스트에 추가
        answer.append(tmp[c[2]-1])
    return answer