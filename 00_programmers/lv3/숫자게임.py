def solution(A, B):
    answer = 0
    N = len(A)  # A==B
    '''
    진다고 승점을 잃는 것은 아니다
    B 팀은 A팀의 카드와 순서를 알고 있다
    한번 이길때마다 승점 1점씩 얻는다
    한번 이길때 가장 작은 차이가 나는 수로 이기는게 좋겠다
    즉, 각 게임마다 가장 적은 비용으로 이기는 것,,
    '''
    # 각 A의 원소에 대해서, 어떻게 B원소들을 매칭시킬까

    A, a_idx = sorted(A), 0
    B, b_idx = sorted(B), 0

    # b_idx >= a_idx 상태를 항상 유지한다
    while b_idx < N:
        # 현재 b_idx로 a_idx를 이길 수 있는가?
        if A[a_idx] < B[b_idx]:
            answer += 1 # 승점 추가
            a_idx += 1
            b_idx += 1
        # 이길 수 없다, 더큰 수로 이겨보자
        else:
            b_idx += 1


    return answer