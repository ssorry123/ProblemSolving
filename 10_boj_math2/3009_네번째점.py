# r1c1, r1c1, r2c1, r2c2
loc_x = list()
loc_y = list()
for _ in range(3):
    tmp = [(int)(i) for i in input().split()]
    loc_x.append(tmp[0])
    loc_y.append(tmp[1])

x = y = 0
loc_x.sort()
loc_y.sort()

if loc_x[0] == loc_x[1]:
    x = loc_x[2]
else:
    x = loc_x[0]

if loc_y[0] == loc_y[1]:
    y = loc_y[2]
else:
    y = loc_y[0]

print(x, y)

