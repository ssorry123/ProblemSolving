def divide(s, idx):
    HEAD = NUMBER = ''

    NUMBER_start = NUMBER_end = -1
    for i in range(len(s)):
        if s[i].isdigit():
            NUMBER_start = i
            NUMBER_end = i + 1
            
            for j in range(i+1, i+6):
                if j >= len(s):
                    break
                if s[j].isdigit():
                    NUMBER_end += 1
                else:
                    break
            break
    
    HEAD = s[ : NUMBER_start].lower()
    NUMBER = int(s[NUMBER_start : NUMBER_end])

    return (HEAD, NUMBER, idx)


def solution(files):
    answer = []

    other_list = []
    for idx, f in enumerate(files):
        other_list.append(divide(f, idx))
    

    # HEAD기준(대소문자 구분 안함), 그 다음 NUMBER 기준, 그 다음 들어온 순서순
    other_list = sorted(other_list, key = lambda x : (x[0], x[1], x[-1]) )
    
    for other in other_list:
        idx = other[-1]
        answer.append(files[idx])

    return answer