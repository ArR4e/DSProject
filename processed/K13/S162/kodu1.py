def auto_hind(hind,vanus):
    if vanus==0:
        return hind
    else:
        return round(auto_hind(hind*0.8,vanus-1),2)
print(auto_hind(10000,6))