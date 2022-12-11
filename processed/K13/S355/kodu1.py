def auto_hind(carprice, aastad):
    autohind = (carprice)*(0.8)**aastad
    if aastad == 0:
        return carprice
    if aastad < 1:
        return 1
    else:
        hind = auto_hind(carprice*0.8,aastad-1)
        return round(autohind,2)
    

        
aastad = 2
carprice = 6788.46
whoa = auto_hind(carprice, aastad)
print(whoa)