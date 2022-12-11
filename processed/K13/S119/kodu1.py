def auto_hind(hind, aastat):
    if aastat == 0:
        return hind
    else:
        return auto_hind(round(hind*0.8,2), aastat - 1)
print(auto_hind(10000.0, 5))