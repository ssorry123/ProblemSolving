def solution(s):
    # int로 매핑해줘야함
    # -1, -2, -3, -4 가 str이면
    # -1, -2, -3, -4 로 정렬된다
    s = list(map(int, s.split()))
    s = sorted(s)
    print(s)

    return str(s[0]) + " " + str(s[-1])

