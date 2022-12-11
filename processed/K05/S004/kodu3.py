def moos(a,b,c):
    loendur=0
    for x in range(a):
        if c>=5:
            c=c-5
            loendur+=1
    for x in range(b):
        if c>=1:
            c=c-1
            loendur+=1
    if c>0:
        return(-1)
    return(loendur)
