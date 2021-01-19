# 삽입 삭제할때마다 정렬하므로 nlogn여서 비효율적인것 같지만
# 통과는 했다
def solution(operations):
    answer = []
    global s
    s = list()
    
    for oper in operations:
        op, i = oper.split()
        
        if op=='I':
            s.append(int(i))
        elif op=='D':
            if len(s)==0:
                continue
            elif i=='1':
                s.sort()
                del s[-1]
            elif i=='-1':
                s.sort()
                del s[0]
    
    print(s)
    if len(s) == 0:
        return [0,0]
    s.sort()
    return [s[-1], s[0]]