a = input().split(' ')
a = [(int)(i) for i in a]
a, b, c = a


def pow(a, b, c):
    """
    pow(int a, int b) % int c
    """
    if b == 1:
        return a % c
    else:
        # a^b = a^b/2 * a^b/2
        if b%2 == 0:
            half = pow(a, (int)(b/2), c)
            return ( (half % c) * (half % c) ) % c
        # a^b = a^b-1 * a
        else:
            b_1 = pow(a, (int)(b-1), c)
            return ( (b_1 % c) * (a % c) ) % c


print(pow(a,b,c))