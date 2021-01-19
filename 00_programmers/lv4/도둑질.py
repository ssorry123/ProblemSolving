# 모든 문제는 2^n으로 풀 수 있다는 것을 기억하자
# 2^n으로 풀라는 것이 아니라
# 하나 하나 변수마다 선택하거나 선택하지 않는 경우가 있다는 것
def solution(money):
    answer = 0
    # 한 집을 털면 다음 집은 반드시 넘어간다
    # n=3부터다
    # DP지만, 처음과 끝 모두 선택할 수 없다
    # 첫집을 선택하면 마지막집을 선택 못하고
    # 마지막집을 선택하면, 첫집을 선택 못한다
    
    # dp[i] 는 money부터 i번째 집까지 선택한 경우
    
    if len(money)==3:
        return max(money)
    
    # 첫집을 반드시 터는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = money[0]
    dp1[2] = money[0]
    for i in range(3, len(money)):
        # i번째 집은 선택할 수 없다
        # i-1번째 집을 선택하거나, 선택하지 않는 경우 두가지가 있다
        a = dp1[i-2] + money[i-1]
        b = dp1[i-1]
        dp1[i] = max(a, b)
    
    # 마지막 집을 반드시 터는 경우
    money.reverse()
    dp2 = [0] * len(money)
    dp2[0] = money[0]
    dp2[1] = money[0]
    dp2[2] = money[0]
    for i in range(3, len(money)):
        a = dp2[i-2] + money[i-1]
        b = dp2[i-1]
        dp2[i] = max(a, b)
    
    return max(dp1[-1], dp2[-1])
