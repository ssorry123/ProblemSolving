def calculator(exp, prior):

    # 우선순위대로
    for op in prior:
        idx = 0
        while idx < len(exp):
            c = exp[idx]
            if c == op:
                exp[idx-1] = eval(str(exp[idx-1]) + c + str(exp[idx+1]))
                del exp[idx]
                del exp[idx]
                # print(exp)
            else:
                idx += 1
    
    # 결과가 한개가 아니라면, 잘못됨
    if len(exp) != 1:
        return False

    return exp[0]


def solution(expression):
    answer = 0

    exp = []

    # 피연산자와 연산자 구분
    start = 0
    for i in range(len(expression)):
        c = expression[i]
        if c in ['+', '-', '*']:
            exp.append(int(expression[start:i]))
            exp.append(c)
            start = i+1
    exp.append(expression[start:])
    # print(exp)

    # 6개의 우선순위
    arr = [
        ['+', '-', '*'], ['+', '*', '-'],
        ['-', '+', '*'], ['-', '*', '+'],
        ['*', '+', '-'], ['*', '-', '+']
    ]

    # 우선순위에 따라 계산해보고, 절대값 최대 찾기
    for prior in arr:
        tmp = abs(calculator(exp.copy(), prior))
        answer = max(answer, tmp)

    print(answer)
    return answer

solution("100-200*300-500+20")
solution("50*6-3*2")