def erinevad_sümbolid(sone):
    symbolid=set(sone)
    return symbolid

def sümbolite_sagedus(sone):
    sagedus ={}
    for arv in sone:
        sagedus[arv]=sagedus.get(arv, 0)+ 1
    return sagedus

def grupeeri(sone):
    taishaalikud=("a","e","i","o","u","õ","ä","ö","ü","A","E","I","O","U","Õ","Ä","Ö","Ü",)
    kaashaalikud=("b","d","f","g","h","i","j","k","l","m","n","p","r","s","š","z","ž","t","v","x","y","q","w","c","B","D","F","G","H","I","J","K","L","M","N","P","R","S","Z","T","V","X","Y","Q","W","C")
    grupeeri={}
    grupeeri["Täishäälikud"]=set()
    grupeeri["Kaashäälikud"]=set()
    grupeeri["Muud"]=set()
    
    sagedus=sümbolite_sagedus(sone)
    for m in sagedus.items():
        if m[0] in taishaalikud:
            grupeeri["Täishäälikud"].add(m)
        elif m[0] in kaashaalikud:
            grupeeri["Kaashäälikud"].add(m)
        else:
            grupeeri["Muud"].add(m)
    return grupeeri
        