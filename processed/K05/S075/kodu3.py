def moos(suur,väike,kogus):
    karp=0
    if kogus-suur*5-väike<=0 and bool(kogus%5<=väike)==True:
        while int(kogus)-5>=0:
            if int(suur)>0:
                karp+=1
                kogus=int(kogus)-5
                suur=int(suur)-1            
            else:
                break
        while int(kogus)-1>=0:
            if int(väike)>0:
                karp+=1
                kogus-=1
                väike-=1
            else:
                break
        return(karp)
    else:
        return(-1)
                        
#moos(3,5,12)