def toM(s):
    s = s.split(':')
    ret = int(s[0])*60 + int(s[1])
    return ret

def convert(info):
    info = info.split(',')

    DUR_TIME = toM(info[1]) - toM(info[0])
    SUBJECT = info[2]

    # '#' 구분
    m = info[3]
    MELODY = list()
    n = len(m)
    i = 0
    while i < n:
        # 다음 문자에 #이 있다면
        if i+1 < n and m[i+1] == '#':
            MELODY.append(m[i:i+2])
            i+=2
        else:
            MELODY.append(m[i])
            i+=1

    # 실제로 재생됬던 구간 str 만들기
    PLAYING = ''
    n = len(MELODY)
    for i in range(DUR_TIME):
        PLAYING += (MELODY[i%n] + '_')
  
    
    return (SUBJECT, DUR_TIME, PLAYING)


def solution(melody, musicinfos):
    answer = ''

    # melody를 #을 구분하여 만든다
    n = len(melody)
    i = 0
    m = ''
    while i < n:
        if i+1 < n and melody[i+1] == '#':
            m += (melody[i:i+2] + '_')
            i+=2
        else:
            m += (melody[i] + '_')
            i+=1


    # 일치하는 노래만 ret에 넣는다
    ret = []
    for idx, music in enumerate(musicinfos):
        tmp = convert(music)
        
        if m in tmp[-1]:
            # 재생 시간, 입력 순서, 노래 제목
            ret.append((tmp[1], idx, tmp[0]))
            
    
    # 없을 경우 (None)을 출력한다, 주의 ( `(None)` 이 아니다 )
    if len(ret) == 0:
        return '(None)'
    
    # 재생 시간 긴 순, 입력된 순
    ret = sorted(ret, key = lambda x : (-x[0], x[1]))

    answer = ret[0][-1]
    return answer