def sõiduplaanlistiks(failinimi):
    f = open(failinimi)
    plaan = []
    for rida in f:
        r = rida.strip().split(' ')
        plaan.append(r)
    f.close()
    return plaan

def kiireimsõit(jrj):
    pass

def kalleimsõit(jrj):
    for el in jrj:
        x = int(el[2])
        for el in jrj:
            y = int(el[2])
            if x < y:
                x = y
    for a in jrj:
        x = str(x)
        if a[2] == x:
            jrj.remove(a)
    return jrj
            
failinimi = input("sisesta failinimi: ")
a = sõiduplaanlistiks(failinimi)
b = kiireimsõit(a)
c = kalleimsõit(a)
print(c)
