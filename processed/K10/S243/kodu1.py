#1. teksti analüüs

def erinevad_sümbolid(lause):
    hulk=set(lause)
    return hulk

def sümbolite_sagedus(lause):
    järjend=list(lause)
    sõnaraamat={}
    for täht in järjend:
        if täht in sõnaraamat:
            sõnaraamat[täht]+=1
        else:
            sõnaraamat[täht]=1
    return sõnaraamat

def grupeeri(lause):
    täis={}
    kaas={}
    muud={}
    täishäälikud=("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü")
    kaashäälikud=("B","C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "S", "T", "V", "X", "Z", "H", "R", "W", "Y")
    for täht in lause:
        if täht.lower() in täishäälikud:
            if täht in täis:
                täis[täht]+=1
            else:
                täis[täht]=1
        elif täht.upper() in kaashäälikud:
            if täht in kaas:
                kaas[täht]+=1
            else:
                kaas[täht]=1
        elif täht not in täishäälikud and täht not in kaashäälikud:
            if täht in muud:
                muud[täht]+=1
            else:
                muud[täht]=1
    hulk={}
    sõnastik={"Täishäälikud": set(täis.items()), "Kaashäälikud": set(kaas.items()), "Muud": set(muud.items())}
    return sõnastik
    
lause="sõida tasa üle silla"
print(grupeeri(lause))