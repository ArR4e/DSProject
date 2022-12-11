def auto_hind(hind, aasta):
    if aasta > 0:
        hind=hind*0.8
        hind=round(hind, 2)
        aasta=aasta-1
        auto_hind(hind, aasta)
    elif aasta == 0:
        return(hind)
auto_hind(8000.0, 5)