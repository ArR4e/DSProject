def  auto_hind(hind, aastaid):
    if aastaid == 0:
        return round(float(hind), 2)
    else:
        return round(auto_hind(hind, aastaid-1) * 0.8, 2)
        

print(auto_hind(10000, 6))

    
    