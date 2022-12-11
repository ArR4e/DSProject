def moos(a, b, c):
    karbid = 0
    for i in range(a+b+1):
        if c >= 5 and a > 0:
            a -= 1
            karbid += 1
            c -= 5
        elif c > 0 and b > 0:
            b -= 1
            karbid += 1
            c -= 1
        elif c == 0:
            return karbid
        else:
            return -1