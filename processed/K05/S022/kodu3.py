def moos(suur, vaike, mass):
    arv = 0
    if mass // 5 > suur:
        mass = mass - suur*5
        arv = arv + suur
    elif mass // 5 <= suur:
        taisosa = mass // 5
        mass = mass - taisosa*5
        arv = arv + taisosa
    if mass // 1 > vaike:
        mass = mass - vaike*1
        arv = arv + vaike
    elif mass // 1 <= vaike:
        taisosa = mass // 1
        mass = mass - taisosa*1
        arv = arv + taisosa
    if mass == 0:
        return arv
    elif mass != 0:
        return -1

print(moos(5, 0, 30))