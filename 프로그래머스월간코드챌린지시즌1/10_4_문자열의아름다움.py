''' 대회 당시 41.2 시간초과, 다시풀어보자 ''' 

str1 = ''
# mid의 아름다움이 가능한지 반환
def can(left, right, mid):
    global str1
    size = right - left + 1

    for m in range(mid, size):
        # 상대 위치(시작 위치)
        for i in range(size - m):
            if str1[left + i] != str1[left + i + m]:
                return True

    return False

# 설마,, 2진탐색쓰..?
def get_beauty(left, right):
    global str1
    # 양끝부터 해보자
    low = 0
    high = right-left
    
    if right == left:
        return 0

    while low <= high:
        mid = int((low+high)//2)

        # 할 수 있다면, 더 큰값의 아름다움이 가능한지 해보자
        if can(left, right, mid):
            low = mid + 1
        else:
            high = mid - 1

    if high < 0:
        return 0
    return high
    

def solution(s):
    answer = 0
    global str1
    str1 = s

    n = len(s)
    zero = True
    for i in range(n):
        if s[0] != s[i]:
            zero = False
            break
    if zero == True:
        return 0

    cache = dict()
    for i in range(n):
        for j in range(i, n):
            k = get_beauty(i, j)
            answer += k
            # print(str1[i:j+1], k)
            
    print(answer)
    return answer

solution('baby')