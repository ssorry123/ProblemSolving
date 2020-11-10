def solution(n, words):
    # 몇 번째 사람이 탈락하는지
    # 그리고 탈락하는 사람은 몇 번째 말한 건지

    talked = dict()

    before_char = words[0][0]
    idx = 0 # 현재 말하고 있는 사람 순서
    idx_round = 0   # 라운드


    ret = True
    for word in words:
        # 끝말잇기 규칙을 지켰는가?
        if word[0] != before_char:
            ret = False
            break
        # 이미 말했었던 단어를 말했는가?
        if word in talked:
            ret = False
            break

        # 규칙을 지켰다면, 처리하고 다음 단어로 넘어감
        before_char = word[-1]
        talked[word] = 0
        idx += 1
        # 한바퀴 돌았다면
        if idx == n:
            idx_round += 1
            idx = 0

    print(ret, idx, idx_round)

    if ret:
        return [0, 0]
    return [idx+1, idx_round+1]