def auto_hind(raha, aastaid):
    if aastaid == 0:
        return raha
    else:
        uus = 0.8 * auto_hind(raha, aastaid - 1)
        return round(uus, 2)
auto_hind(10000.0,5)