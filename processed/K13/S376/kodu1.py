def auto_hind(hind, aasta):
    if aasta == 0:
        return round(hind, 2)
    else:
        return auto_hind(round(0.8 * hind, 2), aasta - 1)