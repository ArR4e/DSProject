def auto_hind(hind, aastatearv):
    if aastatearv <= 0:
        return hind
    if aastatearv > 0:
        aastakulu = float(hind)*0.2
        hind = round(float(hind)-aastakulu, 2)
        aastatearv = aastatearv - 1
        return auto_hind(hind, aastatearv)
    
#print(auto_hind(500, 0))