from decimal import *

def auto_hind(hind, aastad):
    if aastad < 1:
        return round(hind, 2)
    else:
        return round(auto_hind(round(hind*0.8, 2), aastad-1), 2)
print(auto_hind(6788.46,2))