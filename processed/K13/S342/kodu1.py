def auto_hind(hind, aastad):
    if aastad != 0:
        uushind = round((hind - 0.2 * hind), 2)
        uusaastad = aastad - 1
        uushind = auto_hind(uushind, uusaastad)
    else:
        uushind = hind
    return uushind