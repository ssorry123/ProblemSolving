import sys
read = lambda : sys.stdin.readline().strip()

a = [(int)(i) for i in read().split()]
N = a[0]    # 물품의 수             1<=<=100
K = a[1]    # 가져갈 수 있는 총 무게 1<=<=100,000

WV = list() # 물건의 무게와 가치    0<=<=N-1
for _ in range(N):
    a = read().split()
    WV.append([(int)(a[0]), (int)(a[1])])

class Cache:
    # key = 남은무게 * 1000 + 넣을지 말지고민중인아이템번호
    cache = dict()

    @classmethod
    def add(cls, remain_W, item_num, value):
        key = remain_W * 1000 + item_num
        cls.cache[key] = value
    @classmethod
    def check(cls, remain_W, item_num):
        return cls.cache.get(remain_W*1000 + item_num)

def pack(remain_W, item_num):
    """
    pack(int 남은 용량, int 넣을지 고민중인 물건 번호)
    int return 남은 용량에 item_num부터의 물건들을 넣었을 때 최대 가치
    """
    global N, WV
    cache = Cache.check(remain_W, item_num)
    
    # 기저 사례
    if item_num >= N:   # 고민할 아이템이 없는 경우
        return 0
    elif cache != None:
        return cache

    # item_num을 안가져 가는 경우
    ret1 = pack(remain_W, item_num + 1)
    
    # item_num을 가져가기로 결정한 경우
    ret2 = 0
    if remain_W - WV[item_num][0] >=0:
        ret2 = WV[item_num][1] + pack(remain_W - WV[item_num][0], item_num + 1)

    ret = max(ret1, ret2)
    Cache.add(remain_W, item_num, ret)
    return  ret

print(pack(K, 0))
