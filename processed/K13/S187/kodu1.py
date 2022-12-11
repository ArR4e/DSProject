def auto_hind(hind, vanus):
    if vanus == 0:
        return round(hind, 2)
    else:
        return auto_hind(0.8 * hind, vanus - 1)