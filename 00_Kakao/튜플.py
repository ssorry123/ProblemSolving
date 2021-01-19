def solution(s):
    answer = []

    # 가장 큰 괄호 제거
    s = s[1:-1]
    # print(s) => {4,2,3},{3},{2,3,4,1},{2,3}
    

    # 불필요한 괄호 제거 후 숫자 구분
    s = s.split(',{')
    # print(s) => ['{4,2,3}', '3}', '2,3,4,1}', '2,3}']
    s[0] = s[0][1:-1].split(',')
    for i in range(1, len(s)):
        s[i] = s[i][:-1].split(',')
    # print(s) => [['4', '2', '3'], ['3'], ['2', '3', '4', '1'], ['2', '3']]
        
    # 크기순 정렬
    s = sorted(s, key = lambda x:len(x))
    # print(s) => [['3'], ['2', '3'], ['4', '2', '3'], ['2', '3', '4', '1']]
    
    # 추가되지 않은 원소 튜플에 추가
    added = dict()
    for intlist in s:
        for i in intlist:
            if not i in added:
                answer.append(int(i))
                added[i] = 0

    return answer

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")