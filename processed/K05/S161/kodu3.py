suur=1
väike=2
kogus=10
def moos(suur, väike, kogus):
    karbid=0
    while suur>0:
        kogus-=5
        suur-=1
        karbid+=1
        if kogus<0:
            kogus+=5
            karbid-=1
            break
    if väike>=kogus:
        karbid+=kogus
        return karbid
    else:
        return -1
print(moos(suur, väike, kogus))