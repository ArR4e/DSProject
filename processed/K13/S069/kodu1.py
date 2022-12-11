vastus = 0
def auto_hind(hind, aasta):
    global vastus
    vastus = float(hind)
    if aasta == 0:
        vastus = float(hind)
    else:
        vastus = auto_hind(vastus, aasta-1)*0.8
    return round(vastus, 2)
        

