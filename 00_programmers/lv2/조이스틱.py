
def changeChar(targetChar):
    ''' 알파벳을 바꾸는 최소 비용을 반환한다 '''
    initChar = 'A'
    if targetChar == initChar:
        return 0

    ret = 0
    ascii_A = ord('A')  # 65
    ascii_target = ord(targetChar)
    ascii_Z = ord('Z')  # 90

    # 위로 알파벳을 바꿀 경우 필요한 횟수
    to_up = ascii_target - ascii_A
    # 아래로 알파벳을 바꿀 경우 필요한 횟수
    to_down = (ascii_Z + 1) - ascii_target

    return min(to_up, to_down)

needChange = list()
def find_nearTrue(here, name):
    ''' 바꿔야 하는 횟수와, 위치를 반환한다 '''

    global needChange
    # 반환값
    left, left_idx = 1, -1
    right, right_idx = 1, -1
    

    ### 아래 while문은, needChange가 모두 False면 빠져나오지 못한다
    # check right
    while True:
        idx = (here + right) % len(needChange)
        if needChange[idx] == False:    # 바꾸지 않아도 되면
            right += 1
        else:                           # 바꿔야 하는 문자라면
            right_idx = idx
            break
    
    # check left
    while True:
        idx = (here - left) # 음수여도, 파이썬이라 상관 없다
        if needChange[idx] == False:
            left += 1
        else:
            left_idx = idx
            break

    # 반환
    if left<right:
        return left, left_idx
    else:
        return right, right_idx


def solution(name):
    answer = 0
    
    # 문자열을 모두 돌면서, 바꿔야 하는 부분을 체크한다
    global needChange
    needChange = list()
    needChangeCount = 0
    for i in range(len(name)):
        if name[i]=='A':
            needChange.append(False)
        else:
            needChange.append(True)
            needChangeCount += 1

    # 무한 루프에 빠지는 함수가 위에 있으므로, 예외 시킨다
    if needChangeCount == 0:
        return 0



    changedCount = 0
    idx = 0
    while changedCount < needChangeCount:
        # 현재 위치는 바꿀 필요가 없다면, 다음 바꿀 위치를 찾는다
        if needChange[idx]==False:
            cnt, idx = find_nearTrue(idx, name)
            answer += cnt

        # 현재 위치를 바꿔야 한다면,, 바꾸고, 움직인 횟수를 기록한다
        else:
            answer += changeChar(name[idx])
            needChange[idx] = False
            changedCount += 1


    print('answer :: ', answer)
    return answer

solution('JEROEN')
solution('JAN')