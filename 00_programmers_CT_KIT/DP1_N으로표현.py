def solution(N, number):
    answer = -1
    # N을 0개 써서 만들 수 있는 수는 없음
    # N을 1개써서 만들 수 있는 수는 N
    S = [{}, {N}]
    # 1, {N} as n(1)
    # 2, {N}?{N} + {NN} = {5+5, 5-5, 5*5, 5/5} + {55} as n(2)
    # 3, n(1)?n(2) + n(2)?n(1) + {NNN} as n(3)
    #    n(1)?n(2) == n(2)?n(1), when ?==+,*
    # 4, n(1)?n(3) + n(2)?n(2) + n(3)?n(1) + {NNNN} as n(4)
    #    n(1)?n(3) == n(3)?n(1), when ?==+,*
    # n, ....
    # n(4) == n(1)?n(3), n(2)?n(1), n(3)?n(1)의 연산으로만 구하는 이유는
    # n(3) -> n(1)?n(2), n(2)?n(1)의 경우를 포함하고 있고,
    # n(2) -> n(1)?n(1)의 경우를 포함하고 있으므로
    # n(4)를 구할때 n(1)?n(1)?n(2), n(1)?n(1)?n(1)?n(1) 같은 경우는 구하지 않아도 된다
    # 또한 n(1)?n(3)과 n(3)?n(1)의 결과는 *,+일때는 동일하므로
    # n(2)?n(2)까지만 연산하고, -,/의 경우 각 집합의 원소만 바꿔 연산하는 경우를 추가한다

    # N은 8개까지만 사용 가능
    for i in range(2,9):
        # N을 i개 사용하였을때 만들 수 있는 수들
        tmp_set = {int(str(N)*i)}   # 아무런 연산자 없이 이어 붙인것 1
        S.append(tmp_set)
        print(S)
        for k in range(1,i//2 + 1):
            for x in S[k]:
                for y in S[i-k]:
                    S[i].add(x + y)
                    S[i].add(x * y)
                    S[i].add(x - y)
                    S[i].add(y - x)
                    if y!=0:
                        S[i].add(x//y)
                    if x!=0:
                        S[i].add(y//x)

        if number in S[i]:
            answer = i
            break

    return answer