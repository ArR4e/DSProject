def auto_hind(hind, a):
    if a == 0:
        return hind
    else:
        return round((0.8 * auto_hind(hind, a-1)), 2)