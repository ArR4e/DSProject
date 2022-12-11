def auto_hind(hind,aastad):
    if aastad == 0:
        return round(hind,2)
    else:
        return auto_hind(round(0.8*hind,2),aastad-1)

print(auto_hind(6788.46,2))