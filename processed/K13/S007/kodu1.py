def auto_hind(hind, aasta):
    if aasta == 0:
        return round(hind,2)
    else:
        #uus_hind= hind*0.8
        return auto_hind(hind*0.8, aasta-1)
    
print(auto_hind( 6788.46, 2))