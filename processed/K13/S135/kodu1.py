def auto_hind(hind, aastat):
    if aastat == 0:
        return hind
    return auto_hind(round(hind - hind * 0.2, 2), aastat - 1)
