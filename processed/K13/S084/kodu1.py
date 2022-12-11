def auto_hind(hind, aastaid):
    hind = round(hind,2)
    if aastaid > 0:
        return auto_hind(hind-hind*0.2, aastaid-1)
    return hind
print(auto_hind(6788.46,2))