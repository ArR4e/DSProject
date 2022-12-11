def auto_hind(hind, aastad):
    if aastad == 0:
        return round(hind, 2)
    else:
        hind = hind- hind*0.2
        arv = auto_hind(hind, aastad-1)
        return arv
        
print(auto_hind(8000.0, 5))