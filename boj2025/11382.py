inStr= input().strip()

inArr = inStr.split()

answer = 0

for a in inArr:
    answer += int(a)
    
print(answer)
