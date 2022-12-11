def minu_shuffle(a):
    n = len(a)
    for i in range(n):
        suvaline1 = randint(0, n+1)
        suvaline2 = randint(0, n+1)
        a[suvaline1], a[suvaline2] = a[suvaline2], a[suvaline1]
    return a