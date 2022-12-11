def auto_hind(hind, aastad):
    if aastad != 0:
        return auto_hind(round(hind * 0.8, 2), aastad-1)
    return hind
print(auto_hind(8000, 5))
    