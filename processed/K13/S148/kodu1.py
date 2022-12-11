def auto_hind(x, y):
    if y == 0:
        return x
    else:
        return round(auto_hind(x * 0.8, y - 1), 2)