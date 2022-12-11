def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return auto_hind(round(hind-0.2*hind, 2), aastad-1)
    
# hind = 8000.0
# aastad = 5
# print(auto_hind(hind, aastad))