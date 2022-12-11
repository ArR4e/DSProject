#sk- 5kg vk-1kg
def moos(sk,vk,kogus):
    kastid=0
    while kogus!=0:
        if (kogus-5)>=0 and sk>0:
            kogus-=5
            sk-=1
            kastid+=1
            
        elif vk>=1:
            kogus-=1
            vk-=1
            kastid+=1
        else:
            return(-1)
    return(kastid)

            
            