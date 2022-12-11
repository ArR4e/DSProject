def auto_hind(h, a):
    if a == 0:
        return h
    else:
        h = h * 0.8
        h = auto_hind(h, a-1)
        return round(h, 2)