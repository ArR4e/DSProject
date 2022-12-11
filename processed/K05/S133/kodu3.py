import math
def moos(a,b,c): 
    if c > 5*a:
        e=c-(a*5)
        if e>b:
            return(-1)
        elif e<=b :
            return(e + a)
        else:
            return(-1)
    elif c==5*a:
        return(a)
    else:   #c<a*5
        m=c/5
        n=math.floor(m)
        e=c-5*n
        if e>b:
            return(-1)
        elif e<=b :
            return(n + e)
        else:
            return(-1) 
