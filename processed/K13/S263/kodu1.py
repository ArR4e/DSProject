def auto_hind(hind, aastate_arv):
    if aastate_arv == 0:
        return hind
    else:
        uus_hind = hind * (1-(20/100))
        return  round(auto_hind(uus_hind, aastate_arv -1),2)
    
print(auto_hind(10000.0, 6))