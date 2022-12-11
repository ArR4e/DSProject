def moos(a, b, c):
    if b<c%5 or (5*a+b)<c:
        return -1
    else:
        if c//5<=a:
            return (c//5+c%5)
        else:
            return (c-4*a)
