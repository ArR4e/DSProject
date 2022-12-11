def rek_abs(a):
    if isinstance(a, list):
        b=[]
        for el in a:
            b.append(el)
        for i in range(len(a)):
            b[i]=(rek_abs(a[i]))        
    else:
        if a>=0:
            return a
        else:  
            return -a
    return b