def solution(n):
    # iter 가능한 str으로 변환
    # str을 list로 변환
    # list reverse
    # str(chr)를 int로 맵핑
    # map 객체를 list로 변환
    return list(map(int, reversed(list(str(n)))))


print(solution(12345))