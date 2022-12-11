def erinevad_sümbolid(a):
    sõne=set()
    for el in a:
        sõne.add(el)
    return sõne

#print(erinevad_sümbolid(a))

def sümbolite_sagedus(b):
    hulk={}
    for el in b:
        if el in hulk:
            hulk[el]=hulk[el]+1
        else:
            hulk[el]=1
    return hulk

#print(sümbolite_sagedus(b))


def grupeeri(c):
    täis="aiüueöõoä"
    kaas="bdfghjklmnprsztvxcwzqy"
    
    võtmed={"Täishäälikud":{}, "Kaashäälikud":{},"Muud":{}}
    
    for el in c:
        if el.lower() in täis:
        
            if el in võtmed["Täishäälikud"]:
                võtmed["Täishäälikud"][el]=võtmed["Täishäälikud"][el]+1
            else:
                võtmed["Täishäälikud"][el]=1
            
        elif el.lower() in kaas:
            
            if el in võtmed["Kaashäälikud"]:
                võtmed["Kaashäälikud"][el]=võtmed["Kaashäälikud"][el]+1
            else:
                võtmed["Kaashäälikud"][el]=1
        else:
            
            if el in võtmed["Muud"]:
                võtmed["Muud"][el]=võtmed["Muud"][el]+1
            else:
                võtmed["Muud"][el]=1
                
    võtmed["Täishäälikud"]=set(võtmed["Täishäälikud"].items())
    võtmed["Kaashäälikud"]=set(võtmed["Kaashäälikud"].items())
    võtmed["Muud"]=set(võtmed["Muud"].items())
    
    return võtmed


#print(grupeeri(c))
