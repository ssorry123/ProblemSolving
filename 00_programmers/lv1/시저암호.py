def n_shift(c, n):
    # 대문자라 가정
    left = ord('A')
    if c.islower():
        left = ord('a')
    
    # basis를 0으로, ( a가 0 )
    c_idx = ord(c) - left
    # shift 후 basis 이동
    c_shift_idx = (c_idx + n) % 26 + left
    return chr(c_shift_idx)


def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue

        answer += n_shift(s[i], n)

    return answer