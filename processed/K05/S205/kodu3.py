def moos(a,b,c):
    if a*5+b == c:
        return a+b
    elif c%5 > b or a*5+b < c:
        return -1
    elif a==0:
        return c
    elif c-a*5 >=5:
        return a + c-a*5
    else:
        return c//5 + c%5