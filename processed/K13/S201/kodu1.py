def auto_hind(a, n):
    if n == 0:
        return a
    else:
        a *= 0.8
        a = round(a, 2)
        return auto_hind(a, n-1)