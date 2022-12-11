def auto_hind(hind,aastad):
    if int(aastad)>0:
        return auto_hind(float(hind*0.8), int(aastad)-1)
    else:
        return round(hind,2)
        
#print(auto_hind(10000,5))