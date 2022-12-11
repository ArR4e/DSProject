def erinevad_sümbolid(sõne):
    hulk=set()
    for täht in sõne:
        hulk.add(täht)
    return hulk
#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    sõnastik={}
    for täht in sõne:
        if täht in sõnastik:
            sõnastik[täht]=sõnastik[täht]+1
        else:
            sõnastik[täht]=1
    return(sõnastik)
    
    
def grupeeri(sõne):
    täishäälik=["a","e","i","o","u","õ","ä","ö","ü"]
    kaashäälik=["k","p","t","g","b","d","q","w","r","y","s","f","h","j","l","z","ž","š","c","v","n","m"]
    sõnastik={"Täishäälik":{}, "Kaashäälik":{}, "Muud":{}}
    sagedus=sümbolite_sagedus(sõne)
    for i in sagedus.items():
        if i[0].lower() in täishäälik:
            sõnastik["Täishäälik"]=sõnastik["Täishäälik"]+i
        elif i[0].lower() in kaashäälik:
            sõnastik["Kaashäälik"]=sõnastik["Kaashäälik"]+i
        else:
            sõnastik["Muud"]
    return sõnastik

#print(grupeeri("Tere!"))
    