def auto_hind(hind, a):
    if a <= 0:
        return hind
    else:
        return auto_hind(round(hind*0.8, 2), a-1)
        