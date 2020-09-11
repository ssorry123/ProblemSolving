# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# 맵이 조건에 맞는지 확인
def check(mmap):
    # 기둥 검사
    # 기둥 아래가 기둥이거나 보이거나, 바닥이어야 함
    # 보 검사
    # 보 양쪽이 보이거나, 한쪽이나 양쪽이 기둥위에 있어야 함
    for m in mmap:  # 모든 건축물을 조사
        x, y, a = m
        # 기둥이고
        if a==0:
            if y==0: # 바닥에 있는 기둥이라면
                continue
            if (x, y-1, 0) in mmap: # 아래에 기둥이 있다면
                continue
            if (x, y, 1) in mmap or (x-1, y, 1) in mmap:    # 보가 받쳐준다면
                continue
            return False
        # 보 이고
        elif a==1:
            if (x-1, y, 1) in mmap \
                and (x+1, y, 1) in mmap: # 양쪽에 보가 있다면
                continue
            if (x, y-1, 0) in mmap \
                or (x+1, y-1, 0) in mmap:   # 아래에 기둥이 하나라도 있다면
                continue
            return False
    return True

def solution(n, build_frame):
    answer = [[]]
    # mmap 안에, 어떤 원소가 있는지 찾아봐야 하기 때문에
    # (,,) in mmap을 사용할때 효율성을 위해 집합을 사용
    # 리스트로 구현 시 전체 탐색함
    mmap = set()
    for bf in build_frame:
        # a=0 기둥, a=1보, b=0 삭제, b=1 설치
        # 설치나 삭제를 해보고, 이상이 있으면 취소한다
        x, y, a, b = bf
        if b==1:
            mmap.add((x, y, a))
            if check(mmap) == False:
                mmap.remove((x,y,a))
        elif b==0:
            mmap.remove((x, y, a))
            if check(mmap) == False:
                mmap.add((x,y,a))
    
    # 정렬 후 반환
    result = sorted(mmap, key = lambda x:(x[0], x[1], x[2]))
    
    return result

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])