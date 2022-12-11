def erinevad_sümbolid(sõne):
    sümbolid=set()
    for süm in sõne:
        sümbolid.add(süm)
    return(sümbolid)

def sümbolite_sagedus(sõne1):
    sagedus={}
    for süm in sõne1:
        arv=0
        for korduv in sõne1:
            if korduv==süm:
                arv+=1
        sagedus[süm]=arv
    return(sagedus)
        
def grupeeri(sõne2):
    tüübid={}
    esinemine_täishäälikud=set()
    esinemine_kaashäälikud=set()
    esinemine_muud=set()
    for i in sõne2:
        if i in ("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü", "A", "E", "I", "O", "U", "Õ", "Ä", "Ö", "Ü"):
            arv=sõne2.count(i)
            esinemine_täishäälikud.add((i, arv))
        elif i in ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "š", "ž", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z", "Š", "Ž"):
            arv=sõne2.count(i)
            esinemine_kaashäälikud.add((i, arv))
        else:
            arv=sõne2.count(i)
            esinemine_muud.add((i, arv))
    tüübid["Täishäälikud"]=esinemine_täishäälikud
    tüübid["Kaashäälikud"]=esinemine_kaashäälikud
    tüübid["Muud"]=esinemine_muud
    return(tüübid)
    
            
            