def auto_hind(hind, n):
    if n == 0:
        return round(hind, 2)
    else:
        return auto_hind(round(hind * (1 - 0.2), 2), n-1)
    
