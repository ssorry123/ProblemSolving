def solution(A, B):
    A_row = len(A)
    A_col = len(A[0])
    B_row = len(B)
    B_col = len(B[0])

    if A_col != B_row:
        return False
    
    # A_row X B_col
    answer = list()
    for _ in range(A_row):
        answer.append([0]*B_col)
    
    # print(answer)
    for r in range(A_row):
        for c in range(B_col):
            tmp = 0
            for i in range(A_col):
                tmp += A[r][i]*B[i][c]
            answer[r][c] = tmp

    return answer

