def erinevad_sümbolid(sõne):
    sümbolite_hulk = set(sõne)
    return sümbolite_hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for i in sõne:
        sõnastik[i] = sõnastik.get(i, 0) + 1
    return sõnastik

def grupeeri(sõne):
    vokaalid = ["a","e","i","o","u","õ","ä","ö","ü","A","E","I","O","U","Õ","Ä","Ö","Ü"]
    konsonandid = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    grupid = {}
    grupid['Täishäälikud'] = set()
    grupid['Kaashäälikud'] = set()
    grupid['Muud'] = set()
    sümbolid = sümbolite_sagedus(sõne)
    for võti,arv in sümbolid.items():
        if võti in vokaalid:
            grupid['Täishäälikud'].add((võti,arv))
        elif võti in konsonandid:
            grupid['Kaashäälikud'].add((võti,arv))
        else:
            grupid['Muud'].add((võti,arv))
    return grupid