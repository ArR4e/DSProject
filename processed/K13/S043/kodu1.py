def auto_hind(hind, aastad):
    järka = 0.8*hind
    if aastad > 0:
        hind = auto_hind(järka, aastad-1)
    return round(hind, 2)
    
        

print("Vastus:")
print(auto_hind(10000, 6))
