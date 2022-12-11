def auto_hind(hind, aasta):
    if aasta == 0:
        if round(hind,2) >= round(hind+0.001,2):
            return round(hind,2)
        else: 
            return round(hind+0.001,2)
    else:
        return auto_hind(hind*0.8, aasta-1)
#print(auto_hind(6788.46, 2))
#print(auto_hind(10000.0, 1))
#print(auto_hind(8000.0, 5))