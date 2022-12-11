

def auto_hind(hind,aasta):
    if aasta == 0:
        return hind
    else:
        hind = round((hind - 0.2*hind),2)
        aasta -= 1
        return auto_hind(hind,aasta)
    
print (auto_hind(10000,6))
        