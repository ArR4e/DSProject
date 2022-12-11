def moos(suured, väiksed, kogus):
    if kogus-5*suured-väiksed>0:
        return(-1)
    else:
        karpe=0
        while kogus-5>=0 and suured>0:
            karpe=karpe+1
            kogus-=5
            suured-=1
        while kogus>0 and väiksed>0:
            karpe=karpe+1
            kogus-=1
            väiksed-=1
        if kogus>0:
            return(-1)
        else:
            return(karpe)