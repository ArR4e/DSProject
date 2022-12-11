def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    elif aastad != 0:
        hind = hind*0.8
        aastad -= 1
        return round(auto_hind(hind, aastad), 2)
        
print(auto_hind(104510, 5))