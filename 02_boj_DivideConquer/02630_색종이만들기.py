# 입력 받는 부분
N = (int)(input())

puzzle = list()
for i in range(N):
    tmp = (str)(input())
    tmp = tmp.split(' ')
    puzzle.append(tmp)


def print_puzzle(puz):
    print('.............')
    for i in puz:
        print(i)
    print('.............\n')

# 모두 0이거나 1인지 확인하기
def check_puzzle(puz):
    n = len(puz)
    n = n*n

    cnt = 0
    for p in puz:
        cnt += p.count('0') # 흰색 체크
    
    
    if cnt == 0:    # 모두 '1'(파란색)인경우
        return 0, 1
    elif cnt == n:  # 모두 '0'(흰색)인경우
        return 1, 0
    else:
        return None


a = 0
b = 0
def divide(n_puzzle):
    # 퍼즐의 크기 측정
    n = len(n_puzzle)

    # 만약 퍼즐이 모두 같은 색으로 되어 있다면
    ret = check_puzzle(n_puzzle)
    # print(ret)
    if ret != None:
        global a
        global b
        i, j = ret
        a += i
        b += j
        
    else:
        # print_puzzle(n_puzzle)

        div_puzzle_1 = list()
        div_puzzle_2 = list()
        div_puzzle_3 = list()
        div_puzzle_4 = list()

        # 4개로 쪼개기
        for i in range(n):
            n_puz = n_puzzle[i]
            if i < n/2:
                div_puzzle_1.append(n_puz[0 : (int)(n/2)])
                div_puzzle_2.append(n_puz[(int)(n/2) : n])
            else:
                div_puzzle_3.append(n_puz[0 : (int)(n/2)])
                div_puzzle_4.append(n_puz[(int)(n/2) : n])

        # 쪼갠 후 재귀 호출
        divide(div_puzzle_1)
        divide(div_puzzle_2)
        divide(div_puzzle_3)
        divide(div_puzzle_4)
            

divide(puzzle)
print("{0}\n{1}".format(a,b))