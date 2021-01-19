def solution(clothes):
    answer = 0
    
    spy = dict()
    for v, k in clothes:    # 옷, 옷의 종류
        if not k in spy:
            spy[k] = set()
        spy[k].add(v)


    min_k = 1
    max_k = len(spy)
    
    # idx1부터, 옷의 종류에 따른 옷의 개수를 저장
    arr = [0] * (max_k)
    for idx, k in enumerate(spy):
        arr[idx] = len(spy[k])
    print(arr)

    # 0번 종류의 옷 경우의 수 => 선택안함, 하나 선택, 두개 선택, ...
    # 1번 종류의 옷 경우의 수 => 선택안함, 하나선택, ...
    # n번 종류의 옷 경우의 수 => 선택안함, ... ,

    answer = 1
    for n in arr:
        answer = answer*(n+1)
    answer -= 1 # 모두 선택하지 않은 경우를 뺀다
    
    
    return answer