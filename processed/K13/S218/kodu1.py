def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return round(auto_hind(hind-0.2*hind,aastad-1),2)


print(auto_hind(8000,5))