def auto_hind(hind, aastad):
    if aastad<1:
        return round(hind, 2)
    else:
        uus_hind=round(hind*(1-(20/100)),2)
        return round(auto_hind(uus_hind, aastad-1), 2)
