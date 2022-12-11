def auto_hind(alghind,aastat):
    if aastat==0:
        return round(alghind,2)
    else:
        uus_hind=alghind*(1-20/100)
        return round(auto_hind(uus_hind,aastat-1),2)