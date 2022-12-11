import math # 2 4 14
def moos(x,y,kogus):
    xk = x*5 + y
    if xk < kogus: return -1
    if y < kogus and kogus < x*5: return -1
    if x == 0 and y >= kogus: return kogus
    purke = 0
    max_suur = math.floor(kogus/5)
    alles = kogus - max_suur*5
    x_purke = max_suur -x
    if x_purke == 0: purke+=x
    else: purke+=max_suur
    purke+=alles
    return purke