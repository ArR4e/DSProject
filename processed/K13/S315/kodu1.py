def auto_hind(hind, aastad):
    uus_hind = 0.8*hind
    if aastad <= 0:
        return round(hind, 2)
    else:  
        return auto_hind(uus_hind, aastad-1)
        
#kodu1 test4 on katki