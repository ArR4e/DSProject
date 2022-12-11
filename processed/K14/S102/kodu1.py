def rek_abs(a):
    b=[]

    for i in range(len(a)):
        if isinstance(a[i], (float, int)):
            b.append(abs(a[i]))
        else:
            b.append(rek_abs(a[i]))
    return b
                