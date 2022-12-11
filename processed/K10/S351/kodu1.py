def erinevad_sümbolid(sõne):
    hulk=set()
    for element in sõne:
        if element in hulk:
            continue
        else:
            hulk.add(str(element))
    return hulk
        
        
def sümbolite_sagedus(sõne):
    hulk={}
    for element in sõne:
        if element not in hulk:
            hulk[element]=1
        else:
            number=(hulk.pop(element))+1
            hulk[element]=number
    return hulk

    
def grupeeri(sõne):
    sõnestik={}
    for element in sõne:
        if element not in sõnestik:
            sõnestik[element]=1
        else:
            number=(sõnestik.pop(element))+1
            sõnestik[element]=number
    täishäälikud={"A","E","I","O","U","Õ","Ä","Ö","Ü","a","e","i","o","u","õ","ä","ö","ü"}
    kaashäälikud={"q","c","x","B","D","F","G","H","J","K","L","M","N","P","R","S","V","b","d","f","g","h","j","k","l","m","n","p","r","s","š","z","ž","t","v","y","w"}
    muud={"!",".","?"," ",",","-","'"}
    
    vastus={}
    
    väikene_täishäälik=set()
    for täishäälik in täishäälikud:
        if täishäälik in sõnestik:
            väikene_täishäälik.add((täishäälik,sõnestik[täishäälik]))
        else:
            continue
        
    väikene_kaashäälik=set()
    for kaashäälik in kaashäälikud:
        if kaashäälik in sõnestik:
            väikene_kaashäälik.add((kaashäälik,sõnestik[kaashäälik]))
        else:
            continue
    
    väikene_muu=set()
    for muu in muud:
        if muu in sõnestik:
            väikene_muu.add((muu,sõnestik[muu]))
        else:
            continue
    
    vastus["Täishäälikud"]=väikene_täishäälik
    vastus["Kaashäälikud"]=väikene_kaashäälik
    vastus["Muud"]=väikene_muu
    return vastus

    