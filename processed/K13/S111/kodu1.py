def auto_hind(hind, aastad):
    if aastad==0:
        return hind
    else:
        hind=round(float(hind)*0.8,2)
        return auto_hind(hind, aastad-1)

print(auto_hind(10000, 6))