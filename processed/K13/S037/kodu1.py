def auto_hind(hind, aastaid):
    if aastaid == 0:
        return round(hind,2)
    else:
        uus_hind = round(hind*0.8,2)
        aastaid -= 1
        lõplik = auto_hind(uus_hind,aastaid)
        return round(lõplik,2)