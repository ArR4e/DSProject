def erinevad_sümbolid(sõne):
    sõnede_hulk=set(sõne)
    return sõnede_hulk

sõne="hulk ei sisalda kunagi korduvaid elemente"
#print(erinevad_sümbolid(sõne))

def sümbolite_sagedus(sõne):
    sõnastik={}
    sone_järjend=list(sõne)
    for i in range(len(sone_järjend)):
        lugeja=1
        for j in range(len(sone_järjend)):
            if sone_järjend[i]==sone_järjend[j] and i!=j:
                lugeja=lugeja+1
                   
        sõnastik[sone_järjend[i]] =  lugeja
    return sõnastik

sõne="Hei hopsti, väikevend!"
#print(sümbolite_sagedus(sõne))

def grupeeri(sõne):
    täielik_sõnastik={}
#     täishäälikute_sõnasik={}
#     kaashäälikute_sõnasik={}
#     muud_sõnasik={}
    täishäälikute_hulk=set()
    kaashäälikute_hulk=set()
    muud_hulk=set()
    sõnastik=sümbolite_sagedus(sõne)
    täishäälikud="aeiouõäöü"
    kaashäälikud="bcdfghjklmnpqrsšzžtvwxy"
    täishäälikud_järjend=list(täishäälikud)
    kaashäälikud_järjend=list(kaashäälikud)
    for i in range(3):
        
        for el in sõnastik:
            elemendi_järjend=[el, sõnastik[el]]
            elemendi_ennik=tuple(elemendi_järjend)
            if (el.lower()) in täishäälikud_järjend: 
                täishäälikute_hulk.add(elemendi_ennik)
            
            elif (el.lower()) in kaashäälikud_järjend:
               kaashäälikute_hulk.add(elemendi_ennik)
            else:
                muud_hulk.add(elemendi_ennik)
        liba_järjend=["Täishäälikud", "Kaashäälikud", "Muud"]
        hulkade_järjend=[täishäälikute_hulk, kaashäälikute_hulk, muud_hulk]
        täielik_sõnastik[liba_järjend[i]]=hulkade_järjend[i]
#             
#     täishäälikute_sõnasik["Täishäälikud"]=täishäälikute_hulk
#     kaashäälikute_sõnasik["Kaashäälikud"]=kaashäälikute_hulk
#     muud_sõnasik["Muud"]=muud_hulk
#     Kogu_järjend=[täishäälikute_sõnasik, kaashäälikute_sõnasik, muud_sõnasik]
#     kogu_hulk=set()
#     
#    
#     print(täishäälikute_hulk)
#     print(kaashäälikute_hulk)
#     print(muud_hulk)
    
#     print(täishäälikute_sõnasik)
#     print(kaashäälikute_sõnasik)
#     print(muud_sõnasik)
    return täielik_sõnastik
sõne="sõida tasa üle silla" 
print(grupeeri(sõne)) 
