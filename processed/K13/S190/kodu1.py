def auto_hind(hind,aastad):
    if aastad == 0:
        return hind
    return round(0.8 * auto_hind(hind,aastad-1),2)

print(auto_hind(555,0))

    