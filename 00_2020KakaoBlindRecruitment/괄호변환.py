# 올바른 문자열인지 확인하기
def check_right(p):
    if len(p) == 0:
        return True

    st = list()
    for i in range(len(p)):
        c = p[i]
        if c=='(':
            st.append(c)
        elif c==')':
            if len(st) == 0:
                return False
            st.pop(-1)
        else:
            pass

    if len(st)==0:
        print("right")
        return True
    return False


# 균형잡힌 문자열 p
# 올바른 문자열인지 확인하고, 아니라면 올바르게 바꿔서 리턴하기
# 지문에 나와있는 그대로 풀면 된다
def solution(p):
    # 올바른 문자열이라면(빈 문자열 포함)
    if check_right(p):
        return p

    # 올바른 문자열이 아니라면 균형잡힌 두 문자열 u, v로 분리한다
    first = second = 0
    u = ''
    for i in range(len(p)):
        c = p[i]
        if c=='(':
            first += 1
            u += c
        else:
            second += 1
            u += c
        if first == second:
            break
    v = p[2*first:]

    # u가 올바른 문자열인 경우
    if check_right(u):
        ret_sv = solution(v)
        return u + ret_sv
    
    # u가 올바른 문자열이 아닌 경우
    tmp = '(' + solution(v) + ')'
    tmp_attach = ''
    for i in range(1, len(u)-1):
        c = u[i]
        if c=='(':
            tmp_attach += ')'
        else:
            tmp_attach += '('
    answer = tmp + tmp_attach
    
    return answer

print(solution("(()())()"))