
def auto_hind(hind, aastat):
    if aastat == 0:
        return hind
    else:
        lopphind = auto_hind(hind, aastat-1) * 0.8
        return round(lopphind, 2)

auto_hind(10000.0, 5)