#see töötab, kui üksi automaatkontrolli lasta
def erinevad_sümbolid(sõne):
    a = []
    for märk in sõne:
        if märk not in a:
            a.append(märk)
    hulk = set(a)
    return hulk
            

def sümbolite_sagedus(sõne):
    b = {}
    for märk in sõne:
        if märk in b:
           b[märk] = b[märk] + 1
        else:
            b[märk] = 1
    return b


def grupeeri(sõne):
    sõnastik = {}
    kordi = []
    täht = []
    kordik = []
    tähtk = []
    kordim = []
    tähtm = []
    täishäälikud = ["a","e","i","o","u","ü","ö","õ","ä"]
    kaashäälikud = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    for märk in sõne:
        
        if märk.lower() in täishäälikud:
            if märk not in täht:
                täht.append(märk)
                kordi.append(1)
            else:
                kordi[(täht.index(märk))] = kordi[(täht.index(märk))] + 1
    
        elif märk.lower() in kaashäälikud:
            if märk not in tähtk:
                tähtk.append(märk)
                kordik.append(1)
            else:
                kordik[(tähtk.index(märk))] = kordik[(tähtk.index(märk))] + 1
        else:
            if märk not in tähtm:
                tähtm.append(märk)
                kordim.append(1)
            else:
                kordim[(tähtm.index(märk))] = kordim[(tähtm.index(märk))] + 1
    täis = set(list(zip(täht,kordi)))
    kaas = set(list(zip(tähtk,kordik)))
    muu = set(list(zip(tähtm,kordim)))
    sõnastik['Täishäälikud'] = täis
    sõnastik['Kaashäälikud'] = kaas
    sõnastik['Muud'] = muu
                    
    return sõnastik

        

