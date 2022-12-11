def auto_hind(hind, aastad):
    if aastad==0:
        return round(hind,2)
    elif aastad==1:
        return round(hind*0.8,2)
    else:
        return round(auto_hind(hind*0.8, aastad-1),2)
    
    
    
    
print(auto_hind(10000.0, 6))