def erinevad_sümbolid(sõne):   
    return set(sõne)
def sümbolite_sagedus(sõne):
    a = {}
    for x in sõne:
        if x in a:
            a[x]+=1
            
        else:
            a[x]=1
    return a
def grupeeri(sõne):
    täishäälikud="euioüõaöä"+"euioüõaöä".upper()
    kaashäälikud="qwrtypsdfghjklzxcvbnm"+"qwrtypsdfghjklzxcvbnm".upper()
    sett={"Täishäälikud":set(),"Kaashäälikud":set(),"Muud":set()}
    hulk= sümbolite_sagedus(sõne)
    for x in hulk:
        if x in täishäälikud:
            sett["Täishäälikud"].add((x,hulk[x]))
        elif x in kaashäälikud:
            sett["Kaashäälikud"].add((x,hulk[x]))
        else:
            sett["Muud"].add((x,hulk[x]))
    return sett