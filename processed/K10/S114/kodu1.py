def erinevad_sümbolid(sõne):
    vastus = set()
    for i in sõne:
        if i not in vastus:
            vastus.add(i)
    return vastus
    
def sümbolite_sagedus(sõne):
    vastus = {}
    test = set()
    for i in sõne:
        vastus[i] = vastus.get(i,0)+1
    return vastus

def grupeeri(sõne):
    vastus = {}
    vastus["Täishäälikud"] = set()
    vastus["Kaashäälikud"] = set()
    vastus["Muud"] = set()
    
    sagedus = sümbolite_sagedus(sõne)
    täishäälikud = ["a","e","i","o","u","õ","ä","ö","ü","A","E","I","O","U","Õ","Ä","Ö","Ü"]
    kaashäälikud = ["q","c","b","d","f","g","h","j","k","l","m","n","p","r","s","š","z","ž","t","v","w","x","y","z","C","B","D","F","G","H","J","K","L","M","N","P","R","S","Š","Z","Ž","T","V","W","X","Y","Z"]# Tean, pole kõige parem lahendus
    kirjavahemärgid = [",",".","!","?","-","_","="," ","'"]
    sõnastik = {}
    for i in täishäälikud:
        if i in sagedus:
            (u,p) = i,sagedus[i]
            vastus["Täishäälikud"].add((u,p))
    for i in kaashäälikud:
        if i in sagedus:
            (u,p) = i,sagedus[i]
            vastus["Kaashäälikud"].add((u,p))
    for i in kirjavahemärgid:
        if i in sagedus:
            (u,p) = i,sagedus[i]
            vastus["Muud"].add((u,p))

    return vastus
            
#erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente")
#sümbolite_sagedus("Hei hopsti, väikevend!")
grupeeri("Kuule, August! Käes on august?")


