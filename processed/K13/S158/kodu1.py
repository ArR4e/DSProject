def auto_hind(a, b) :
    if b == 0:
        return a
    elif b > 0:
        return round(auto_hind(a - 0.2*a, b-1), 2)