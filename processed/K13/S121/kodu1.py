def auto_hind(hind, aasta):
    if aasta == 0:
        return round(hind, 2)
    if aasta == 1:
        return round(hind*0.8,2)
    aasta -= 1
    return round(auto_hind(hind, aasta)*0.8, 2)
    
        
print(auto_hind(10000.0, 5))
print(auto_hind(8000.0, 5))