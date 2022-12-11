sõne = input("Sisesta sõne: ")

def erinevad_sümbolid(sõne):
    hulk = set()
    sümbolid = list(sõne)
    for i in range(len(sümbolid)):
        hulk.add(sümbolid[i])
        
    return hulk

erinev = erinevad_sümbolid(sõne)


def sümbolite_sagedus(sõne):
    sõnastik = dict()
    sümbolid = list(sõne)
    sümbolid.sort()
    counter = 1
    for i in range(len(sümbolid)):
        if sümbolid[i] in sõnastik:
            counter += 1
            sõnastik[sümbolid[i]] = counter
        else:
            counter = 1
            sõnastik[sümbolid[i]] = 1
            
    return sõnastik
        
sagedus = sümbolite_sagedus(sõne)


def grupeeri(sõne):
    sõnastik1 = dict()
    hulktäis = set()
    hulkkaas = set()
    hulkmuu = set()
    for i in erinev:
        a = sagedus[i]
        if i in "AEIOUÕÄÖÜaeiouõäöü":
            hulktäis.add((i, a))
        elif i in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            hulkkaas.add((i,a))
        else:
            hulkmuu.add((i,a))
        
    sõnastik1["Täishäälikud"] = hulktäis
    sõnastik1["Kaashäälikud"] = hulkkaas
    sõnastik1["Muud"] = hulkmuu
        
    return sõnastik1
print(grupeeri(sõne))