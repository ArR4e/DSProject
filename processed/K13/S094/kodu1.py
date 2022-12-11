
def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        # väheneb 20%.
        uus_hind = hind * 0.8        
        return round(auto_hind(uus_hind, aastad-1), 2)
    