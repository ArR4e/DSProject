def transponeeriK(a):
    tm=[]
    jr=a[0]
    for el in jr:
        tm.append([])
    for j in a:
        i=len(j)-1
        k=0
        while i>=0:
            tm[k].append(j[i])
            i-=1
            k+=1
    for j in tm:
        j.reverse()
    return tm