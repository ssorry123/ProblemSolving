def solution(s):
    answer = 999999
    # 문자열은 제일 앞에서부터, 정해진 길이만큼 잘라야 합니다.
    
    # i = 자를 수 있는 정해진 크기
    for i in range(1, len(s)+1):
        start = 0
        cut = list()
        remain = len(s) #남은 문자열의 개수

        while i <= remain:
            # (잘랐던 적이 있던 것이 있고) 자를 문자열이 가장 최근에 잘랐던 문자열과 같은 경우
            if len(cut)!=0 and cut[-1] == s[start:start+i]:
                cut[-2] += 1
            # 해당 문자열로 처음 자르는 경우
            else:
                cut.append(1)
                cut.append(s[start:start+i])
            start = start + i
            remain -= i
        
        # i만큼 자르고 남은 것 처리
        if remain > 0:
            cut.append(s[start:])
        
        # i만큼 잘라서 만든 문자열
        ret = ''
        for _cut in cut:
            # 1은 생략
            if _cut != 1:
                ret += str(_cut)
        # print(ret)
        answer = min(len(ret), answer)

    return answer

print(solution("abcabcabcabcdededededede"))