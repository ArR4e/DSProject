def rek_abs(n):
    lis=[]
    for i in n:
        if isinstance(i,list):
            lis.append(rek_abs(i))
        else:
            lis.append(abs(i))
    return lis