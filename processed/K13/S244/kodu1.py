def auto_hind(hind, aastate_arv):
    if aastate_arv == 0:
        return hind
    
    if aastate_arv == 1:
        uus_hind = round(hind *(1-(20/100 )), 2)
        return uus_hind
    else:
        return round(auto_hind(hind, aastate_arv -1) * (1-(20/100 )),2)
    
    
    
    
    
hind = float(input('Sisesta auto hind: '))
aastate_arv = int(input('Sisesta aastate arv: '))
print(auto_hind(hind, aastate_arv))