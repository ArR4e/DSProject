def moos(suur,väike,kogus):
    a=0
    b=0
    if kogus==0:
        return 0
    while suur>0 and kogus>=5:
        a+=1
        kogus-=5
        suur-=1
    while väike>0 and kogus>0:
        b+=1
        kogus-=1
        väike-=1
    if kogus>0:
        return -1
    else:
        return a+b