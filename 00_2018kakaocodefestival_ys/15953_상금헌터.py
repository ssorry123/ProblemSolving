T = (int)(input())

#         1,   3,   6,  10, 15,  21
_2017 = (500, 300, 200, 50, 30, 10)
#         1,   3,  7,   15, 31
_2018 = (512, 256, 128, 64, 32)

for _ in range(T):
    ret = 0
    tmp = input().split()
    a = (int)(tmp[0])
    b = (int)(tmp[1])
    if a==0 or a>21:
        pass
    elif a==1:
        ret += _2017[0]
    elif a>1 and a<=3:
        ret += _2017[1]
    elif a>3 and a<=6:
        ret += _2017[2]
    elif a>6 and a<=10:
        ret += _2017[3]
    elif a>10 and a<=15:
        ret += _2017[4]
    else:
        ret += _2017[5]

    if b==0 or b>31:
        pass
    elif b==1:
        ret += _2018[0]
    elif b>1 and b<=3:
        ret += _2018[1]
    elif b>3 and b<=7:
        ret += _2018[2]
    elif b>7 and b<=15:
        ret += _2018[3]
    else:
        ret += _2018[4]
    
    print(ret*10000)
