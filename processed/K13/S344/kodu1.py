def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        i = aastad
        uus_hind = round((hind - (hind * 0.2)), 2)
        i -= 1
        return auto_hind(uus_hind, i)
    
    
print(auto_hind(8000.0, 5))
    