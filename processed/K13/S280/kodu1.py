# RP / 1. Kasutatud auto hind rekursiivselt

def auto_hind(hind,aastaid):
    if aastaid > 0:
        hind = round(hind * 0.8, 2)
        aastaid -= 1
        return auto_hind(hind, aastaid)
    else:
        return hind
    
print(auto_hind(10000.0, 6)) 