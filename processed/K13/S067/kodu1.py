def auto_hind(alghind, aastad):
    hind = alghind
    if aastad == 0:
        return alghind
    return auto_hind(round(alghind - (alghind / 5), 2), aastad - 1)
print(auto_hind(8000.0, 5)) 