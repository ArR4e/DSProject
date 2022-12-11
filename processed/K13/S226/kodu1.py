def auto_hind(hind, aastad):
    if aastad < 1:
        return hind
    else:
        uus_hind = hind * (1 - (20/100))
        return round(auto_hind(uus_hind, aastad-1), 2)

print(auto_hind(8000.0, 5))