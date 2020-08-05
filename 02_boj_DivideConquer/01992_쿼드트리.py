N = (int)(input())

picture = list()
for i in range(N):
    picture.append(input())

# N = 8
# picture = [
#     '11110000',
#     '11110000',
#     '00011100',
#     '00011100',
#     '11110000',
#     '11110000',
#     '11110011',
#     '11110011'
# ]
# print('\n')
# print(picture)


# 0 또는 1로 압축할 수 있으면 0 또는 1 반환
# 할 수 없으면 -1 반환
def compress_picture(n_picture):
    n = len(n_picture)
    n = n*n
    cnt = 0

    for p in n_picture:
        cnt += p.count('0')

    if cnt == n: # 모두 0, 흰색인 경우
        return 0
    elif cnt == 0:  # 모두 1, 검정색인경우
        return 1
    else:       # 섞여있는 경우
        return -1


ret = ""
def divide(n_picture):
    global ret
    n = len(n_picture)
    
    # 한 숫자로 압축 할 수 있는지 확인
    chk = compress_picture(n_picture)

    # 압축할 수 있다면 압축한 숫자로 표시
    if chk != -1:
        ret += (str)(chk)

    # 압축할 수 없다면
    else:
        # 나눠서 압축
        ret += '('

        # 분할
        pic1 = list()
        pic2 = list()
        pic3 = list()
        pic4 = list()
        for i in range(n):
            pic = n_picture[i]
            if i<n/2:
                pic1.append(pic[0 : (int)(n/2)])
                pic2.append(pic[(int)(n/2) : n])
            else:
                pic3.append(pic[0 : (int)(n/2)])
                pic4.append(pic[(int)(n/2) : n])

        # 재귀 호출
        divide(pic1)
        divide(pic2)
        divide(pic3)
        divide(pic4)

        # 나눠서 압축 마무리
        ret += ')'

divide(picture)
print(ret)