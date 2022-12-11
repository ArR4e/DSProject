from math import floor
def moos(suur, väike, kogus):
    if suur * 5 + väike * 1 >= kogus: #kui on piisavalt (suuri ja väikeseid) karpe kokku, kuhu moos tõsta
        skarbid = floor(kogus / 5)
        jääk = floor(kogus % 5) #ehk mitu kg moosi ei mahtunud suurtesse karpidess ära
        vkarbid = floor(jääk / 1) 
        if väike < vkarbid: #kui on liiga vähe väikseid karpe
            return -1
        kokku = skarbid + vkarbid
        return kokku
    else:
        return -1