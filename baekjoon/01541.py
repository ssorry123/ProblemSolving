a = input()
#a = '55-50+40-123+222+132-23-123+12'

a = a.split('-')    # 뺄 수 있을때 많이 뺀다
# print(a)
# print(a[0].split('+'))

def add_str(expression_str):
    tmp = expression_str.split('+')
    ret = 0
    for i in tmp:
        ret += (int)(i)

    return ret

# 가장 처음과 마지막 문자는 숫자이므로 첫번째 수는 반드시 양수
ret = add_str(a[0])
del(a[0])

# -로 분리하고 나온 수들은 모두 빼버리면 된다
for i in a:
    ret -= add_str(i)

print(ret)