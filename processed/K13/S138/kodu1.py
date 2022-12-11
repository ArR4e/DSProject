def auto_hind(hind,aastaid):
    if aastaid > 0:
        return auto_hind(round(0.8*hind,2),aastaid-1)
    else:
        return hind

print(auto_hind(1000,0))
