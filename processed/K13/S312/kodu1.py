
#kaotab iga aasta 20%
def auto_hind(hind, a):
    if a == 0:
        return hind
    else:
        hind = round(0.8*hind, 2)
        return auto_hind(hind, a-1)
    
    
print(auto_hind(8000.0, 5))    
    