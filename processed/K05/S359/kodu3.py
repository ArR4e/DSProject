def moos(skarp,vkarp,kogus):
    skarbid=0
    vkarbid=0
    while kogus>=5 and skarp >0:
        kogus=kogus-5
        skarbid=skarbid+1
        skarp=skarp-1
    if vkarp==0 or kogus<=5:
        while kogus>0:
            if vkarp==0:
                break
                print(-1)
            kogus=kogus-1
            vkarbid=vkarbid+1
            vkarp=vkarp-1
        arv=skarbid+vkarbid   
        if kogus==0:
            print(arv)
        else:
            print(-1)
