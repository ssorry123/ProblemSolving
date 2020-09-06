asc_0 = ord('0')
asc_9 = ord('9')
def check_digit(i):
    i = ord(i)
    if i<=asc_9 and i>=asc_0:
        return True
    return False

SDT = {'S':1, 'D':2, 'T':3}
def solution(dartResult):
    answer = 0
    num_str = ''    # 0~10까지 수 저장
    score = [0,0,0] # 세번의 점수
    score_idx = -1   # 현재까지 입력된 점수의 위치
    for i in range(len(dartResult)):
        c = dartResult[i]
        # 숫자 입력 받기
        if check_digit(c):
            num_str += c
            continue
        # 숫자에 보너스, 입력된 숫자에 보너스를 제곱한 후 저장 
        if c=='S' or c=='D' or c=='T':
            score_idx+=1
            score[score_idx] = (int)(num_str) ** SDT[c]
            num_str = ''    # 입력받는 임시 숫자저장소 초기화
            continue
        # 아차상
        if c=='#':
            score[score_idx] *= -1
            continue
        # 스타상
        if c=='*':
            score[score_idx] *= 2
            # 첫번째 스타상이 아니라면
            if score_idx!=0:
                score[score_idx-1] *= 2
            continue
    
    for s in score:
        answer += s

    return answer