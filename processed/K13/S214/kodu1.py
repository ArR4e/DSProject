def auto_hind(hind,aastad):
    if aastad==0:
        return hind
    else:
        return round(auto_hind(round(hind*0.8,2),aastad-1),2)
