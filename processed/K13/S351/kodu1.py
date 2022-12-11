def auto_hind(hind, aastad):
    if aastad==0:
        return hind
    else:
        väärtus=hind*0.8
        aastad-=1
        return auto_hind(väärtus, aastad)