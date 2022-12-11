def transponeeriK(m):
    a=len(m)
    b=len(m[0])
    t=[]
    for i in range(b):
        rida=[]
        for j in range(a):
            rida+=[m[-1-j][-1-i]]
        t+=[rida]
    return t