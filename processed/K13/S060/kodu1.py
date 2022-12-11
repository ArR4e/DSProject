def auto_hind(hind,a):
    if a==0:
        return hind
    else:
        hind=round(hind*0.8,2)
        return auto_hind(hind,a-1)
print(auto_hind(6788.46,2))