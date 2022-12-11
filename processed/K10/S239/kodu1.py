def erinevad_sümbolid(s):
    sümbolid=set()
    for i in s:
        sümbolid.add(i)
    return sümbolid

def sümbolite_sagedus(s):
    global sümbolid
    sümbolid={}
    for i in erinevad_sümbolid(s):
        sümbolid[i]=0
        for j in s:
            if i==j:
                sümbolid[i]+=1
    return sümbolid

täish=["a","e","i","o","u","õ","ä","ö","ü"]
kaash=["q","w","r","t","y","p","l","k","j","h","g","f","d","s","z","x","c","v","b","n","m"]

def grupeeri(s):
    grupp={"Täishäälikud":{},"Kaashäälikud":{},"Muud":{}}
    täis=set()
    kaas=set()
    muud=set()
    for i in sümbolite_sagedus(s):
        if i.lower() in täish:
            täis.add((i,sümbolid[i]))
        elif i.lower() in kaash:
            kaas.add((i,sümbolid[i]))
        else:
            muud.add((i,sümbolid[i]))
    grupp["Täishäälikud"]=täis
    grupp["Kaashäälikud"]=kaas
    grupp["Muud"]=muud
    return grupp

s="Kaka, pissi, noku, tussu, puuksukoll!!!"
erinevad_sümbolid(s)
sümbolite_sagedus(s)
print(grupeeri(s))