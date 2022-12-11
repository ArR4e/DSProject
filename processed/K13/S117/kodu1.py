#alustasin 23.11.2021 (20:26)
def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    else:
        uus_hind = round(hind * (1 - (20/100)), 2)
        return auto_hind(uus_hind, aasta - 1)