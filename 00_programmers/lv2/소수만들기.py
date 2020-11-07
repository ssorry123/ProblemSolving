import math

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    
    for div in range(2, int(math.sqrt(n))+1):
        if n % div == 0:
            return False
    
    return True

def solution(nums):
    answer = 0

    # nums에서 세개를 합해서 소수인지 확인한다

    n = len(nums)
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                if isPrime(nums[a]+nums[b]+nums[c]):
                    answer += 1

    return answer