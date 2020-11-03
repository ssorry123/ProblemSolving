def solution(nums):
    answer = 0

    # 포켓몬 종류의 수를 구하자
    mon = dict()
    for n in nums:
        if not n in mon:
            mon[n] = 0
    
    # 가져갈 수 있는 포켓몬의 수
    can_bring = len(nums) // 2

    return min(can_bring, len(mon))