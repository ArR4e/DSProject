def erinevad_sümbolid(sõna):
    leitud=[]
    for täht in sõna:
        leitud.append(täht)
    return set(leitud)

#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõna):
    d={}
    for täht in sõna:
        if täht in d:
            d[täht]=d[täht]+1
        else:
            d[täht]=1
    return d

#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõna):
    täishäälikud=("a","e","i","o","u","õ","ä","ö","ü")
    kaashäälikud=("k","g","p","b","t","d","f","h","j","q","w","r","y","s","l","z","x","c","v","n","m","š","ž")
    d={"Täishäälikud":{}, "Kaashäälikud":{}, "Muud":{}}
    midagi=sümbolite_sagedus(sõna)
    for i,j in midagi.items():
        if i.lower() in täishäälikud:
            d["Täishäälikud"]=d["Täishäälikud"] + (i,j)
        elif i.lower() in kaashäälikud:
            d["Kaashäälikud"]=d["Kaashäälikud"] + (i,j)
        else:
            d["Muud"]=d["Muud"] + (i,j)
    return d

#print(grupeeri("Tere!"))