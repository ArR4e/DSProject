def auto_hind(x, y):
    if y <= 0:
        return x
    else:
        return auto_hind(round(0.8 * x, 2), y - 1)
