def auto_hind(väärtus,aastad):
    if aastad == 0:return round(väärtus,2)
    elif aastad>0:return auto_hind(väärtus*0.8,aastad-1)