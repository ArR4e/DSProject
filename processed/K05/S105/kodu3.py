def moos(a,b,c):
    i=0
    j=0
    purke=0
    
    if c==0:
        return purke
    
    while a>0:
        c=c-5
        a=a-1
        i=i+1
        if c<=5 or a==0:
            purke=purke+i
            break
        
    
    if c==0:
        return purke

    while b>0:
        c=c-1
        b=b-1
        j=j+1
        if c==0:
            purke=purke+j
            return purke
            break
        
    if c==0:
        return purke
       
    return -1

print(moos(4,5,0))
        