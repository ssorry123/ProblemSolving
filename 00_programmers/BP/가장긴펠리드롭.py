# 문제에서 부분 문자열이란 substring을 말하는 거였음..
# 건너뛰어 가는 부분 수열이랑 헷갈렸다..

def maxPali(mid, s):
    # 홀수 길이의 팰린드롬 개수를 세자
    retodd = 1
    diff = 1
    while mid - diff >= 0 and mid + diff < len(s):
        if s[mid - diff] == s[mid + diff]:
            retodd += 2
            diff += 1
        else:
            break
    
    # 짝수개 팰린드롬 세기 전에 검사
    if mid+1 >= len(s):
        return retodd
    # 짝수 검사를 시작할 수 있으면
    if s[mid] != s[mid+1]:
        return retodd
    
    # 짝수길이의 팰린드롬 개수를 세자
    reteven = 2
    left = mid - 1
    right = mid + 2

    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            reteven += 2
            left -= 1
            right += 1
        else:
            break
    
    return max(reteven, retodd)


def solution(s):
    answer = 0

    for mid in range(len(s)):
        ret = maxPali(mid, s)
        answer = max(ret, answer)

    print(answer)
    return answer


solution('abcdcba')