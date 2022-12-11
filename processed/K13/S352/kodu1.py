def auto_hind(hind, aastaid):
    if aastaid==0:
        return hind
    else:
        return auto_hind(round(hind*0.8,2),aastaid-1)

print(auto_hind(8000.0, 5))