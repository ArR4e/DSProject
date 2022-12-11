def auto_hind(hind,aastad):
    if aastad > 0:
        return auto_hind(0.8*hind,aastad-1)
    return round(hind,2)

print(auto_hind(6788.46,2))