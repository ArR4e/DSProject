def auto_hind(hind, aastad):
    uus_hind = hind * (1 - (20 / 100))
    if aastad == 0:
        return hind
    else:
        return round(auto_hind(uus_hind, aastad - 1) ,2)
    

auto_hind(10000.0, 5)