def auto_hind(hind, vanus):
    if vanus == 0:
        return hind
    else:
        return round(auto_hind(round(hind * (1-0.2), 2), vanus-1), 2)
