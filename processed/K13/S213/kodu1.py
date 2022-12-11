def auto_hind(hind, aastad):
    if aastad == 0:
        return float(hind)
    else:
        return auto_hind(round(float(hind * 0.8),2), aastad - 1)
    
print(auto_hind(6788.46,2))