def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return auto_hind(round(hind - 0.2 * hind, 2), aastad - 1)

#print(auto_hind(10000.0, 1))