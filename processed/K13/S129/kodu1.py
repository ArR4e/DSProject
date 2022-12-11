# kasutatud auto


def auto_hind(alghind, aastad):
    if aastad == 0:
        return round(float(alghind), 2)
    else:
        return auto_hind(alghind - alghind*0.2, aastad-1)
    
print(auto_hind(10000.0, 6))