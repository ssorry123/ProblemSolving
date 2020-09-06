import math

# a~z 인지 확인한다
def check_alpha(c):
    a = ord('a')
    z = ord('z')
    if ord(c) <= z and ord(c) >= a:
        return True
    return False

# string을 받아서 dict 형식의 집합을 반환한다
# dict의 key는 원소 값, value는 원소의 개수(중복 허용)
def make_set_dict(sss):
    s1set = dict()
    s1 = ''
    for i in range(len(sss)):
        c = sss[i]
        # 영문자인경우
        if check_alpha(c):
            s1 += c
        # 영문자가 아닌 경우 초기화
        else:
            s1 = ''

        # 영문자 두개를 만든 경우, 같은 원소가 이미 있다면 카운트 증가
        if len(s1) == 2:
            if s1 in s1set:
                s1set[s1] += 1
            else:
                s1set[s1] = 1
            s1 = s1[1] # 두글자 중 뒷글자부터 다시 시작
    return s1set

# 합집합
def UNION(str1, str2):
    # s2에 있는 원소들을 s1로 합친다
    s1 = make_set_dict(str1)
    s2 = make_set_dict(str2)
    for k in s2:
        if k in s1:
            s1[k] = max(s1[k],s2[k])
        else:
            s1[k] = s2[k]
    return s1

# 교집합
def JOINT(str1, str2):
    s1 = make_set_dict(str1)
    s2 = make_set_dict(str2)
    ret = dict()
    for k in s2:
        if k in s1:
            ret[k] = min(s1[k], s2[k])
    return ret

def solution(str1, str2):
    answer = 0
    # 대문자 소문자로 통일
    str1 = str1.lower()
    str2 = str2.lower()
    #print(str1, str2)

    s1s2Union = UNION(str1, str2)
    s1s2Joint = JOINT(str1, str2)
    # 모두 공집합인 경우 (합집합이 없는 경우)
    if len(s1s2Union) == 0:
        return 65536

    ja = 0
    for j in s1s2Joint:
        ja += s1s2Joint[j]
    mo = 0
    for m in s1s2Union:
        mo += s1s2Union[m]
    
    answer = math.floor(ja / mo * 65536)

    return answer

print(solution('FRANCE', 'french'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('handshake', 'shake hands'))
print(solution('E=M*C^2', 'e=m*c^2'))