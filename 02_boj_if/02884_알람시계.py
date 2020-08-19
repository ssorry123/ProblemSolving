a = [(int)(i) for i in input().split()]
H = a[0]
M = a[1]

if M >= 45:
    print(H, M-45)
else:
    M = M + 15
    H = H - 1
    if H < 0:
        H = 23
    print(H, M)
