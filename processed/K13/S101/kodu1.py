def auto_hind(hind,aastad):
    if aastad==0:
        return hind
    else:
        hind=round(hind*0.8,2)
        aastad-=1
        return auto_hind(hind,aastad)

print(auto_hind(10000.0,1))