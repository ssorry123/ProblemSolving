''' 대회 당시 AC '''

# 2진 변환을 다르게 하기
def solution(s):
    # 첫번째 위치에는 이진변환 횟수
    # 두번째 위치에는 변환과정에서 제거된 0의 개수
    answer = [0, 0]

    while s!='1':
        cnt0 = 0
        for i in range(len(s)):
            if s[i] == '0':
                cnt0+=1
        
        # 0 모두 제거
        s = '1' * (len(s)-cnt0)

        # s = s의 길이를 2진법으로
        s = str(format(len(s), 'b'))
        
        answer[0] += 1
        answer[1] += cnt0


    return answer

solution('0111010')
