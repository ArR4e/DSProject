def auto_hind(alg_hind,aasta):
    if aasta == 0:
     return alg_hind
    else:
        return auto_hind(round(alg_hind - alg_hind*0.2,2),aasta - 1)
    
print(auto_hind(10000.0,0))
