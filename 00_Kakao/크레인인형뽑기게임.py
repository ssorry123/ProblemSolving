def solution(board, moves):
    answer = 0

    # 인형을 뽑고 담아놓는 바구니 (스택)
    bucket = list()

    for move in moves:
        idx = move - 1
        item = 0

        # idx 위치에서 집게 한칸씩 내려가면서 인형뽑기
        for depth in range(len(board)):
            # 인형이 있으면
            if board[depth][idx] != 0:
                # 인형 뽑기
                item = board[depth][idx]    
                board[depth][idx] = 0
                break
        
        # 인형을 뽑은게 없다면
        if item == 0:
            continue

        # 바구니에 인형 넣기
        # 바구니가 비어있다면 그냥 넣는다
        if len(bucket) == 0:
            bucket.append(item)
        # 바구니의 가장 위 인형이 뽑은 인형과 같다면
        elif bucket[-1] == item:
            # 인형 터트리고, 터진 인형 개수 기록
            del bucket[-1]
            answer += 2
        # 같지 않다면
        else:
            bucket.append(item)
            

    return answer