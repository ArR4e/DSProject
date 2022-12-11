def auto_hind(hind, aa):
    if aa < 1:
        return hind
    uhind = round((hind * 0.8), 2)
    return auto_hind(uhind, aa - 1)
