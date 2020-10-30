import math

def solution(w, h):
    '''
    기울기 8/12 는 2/3과 마찬가지,,
    최대 공약수는 4
    대각선은 2*3블록이 4개 있는 것과 같다

    블록을 나눴을때, 블록 내에서 직선은
    (정수, 정수)인점을 절대로 지나지 않는다
    '''

    # if 2개 -> testcase (7,8,9,11,12,14,18) 통과
    if w == 1 or h == 1:
        return 0
    if w == h:
        return w * (h-1)

    block_cnt = int(math.gcd(w, h))
    print(block_cnt)
    w1, h1 = int(w / block_cnt), int(h / block_cnt)
    cant_use = (w1 + h1 - 1) * block_cnt
    return w*h - cant_use


# 50점, 왜지
def solution1(w,h):
    # 자른 것 두개를 합치면 또 하나의 직사각형이 된다
    # 너비는 변하지 않고 높이가 줄어든다
    # 높이는 얼마나 줄어드는가 ?..?

    # 또, 너비가 변하지 않으려면 기울기가 1이상이어야 너비가 변하지 않는다
    if w > h:
        tmp = w
        w = h
        h = tmp
    diff = h/w
    diff1 = math.ceil(diff)

    h -= int(diff1)
    return w * h
    
