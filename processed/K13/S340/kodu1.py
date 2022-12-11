def auto_hind(hind,aastaid):
    if aastaid==0:
        return hind
    else:
        hind=round(hind*((1-(20/100))),2)
        return auto_hind(hind,aastaid-1)
    
auto_hind(15000.0, 3)
    