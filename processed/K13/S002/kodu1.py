def auto_hind(hind, a):
    if a == 0:
        return hind
    else:
        return auto_hind(round(hind*0.8,2),a-1)
        
auto_hind(10000.0, 0)
auto_hind(10000.0, 5)
auto_hind(10000.0, 1)
auto_hind(8000.0, 5)
auto_hind(10000.0, 6)