from string import *

def erinevad_sümbolid(fraas):
    hulk=set(fraas)
    return(set(hulk))
#erinevad_sümbolid("kontroll, asd")

def sümbolite_sagedus(fraas):
    kogused={}
    for i in list(fraas):
        if i in kogused:
            kogused[i]=int(kogused[i])+1
        else:
            kogused[i]=int(1)
    #print(kogused)
    return kogused
#sümbolite_sagedus("Hei hopsti, väikevend!")

def grupeeri(fraas):
    Täishäälikud={}
    Kaashäälikud={}
    Muud={}
    sagedus=sümbolite_sagedus(fraas)
    for i in erinevad_sümbolid(fraas):
        try:
            if i.lower() in "aeiouõäöü":
                Täishäälikud[i]=sagedus[i]
            elif i.lower() in ascii_lowercase:
                Kaashäälikud[i]=sagedus[i]
            elif i==" ":
                Muud[i]=sagedus[i]
        except:
            Muud[i]=sagedus[i]
    grupid={"Täishäälikud":dict(Täishäälikud), "Kaashäälikud":dict(Kaashäälikud), "Muud":dict(Muud)}
    print(grupid)
    return grupid
grupeeri("sõida tasa üle silla")
        