t={"i","ü","u","e","ö","õ","o","ä","a","A"}
k={"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","š","z","ž","t","v","w","x","y","K","L","M"}
def erinevad_sümbolid(sona):
    a=set(sona)
    return a
def sümbolite_sagedus(sona):
    vastus={}
    a=set(sona)
    for rida in a:
        kordi=sona.count(rida)
        vastus[rida]=kordi
    return vastus
def grupeeri(sona):
    vastus={}
    tais=set()
    kaas=set()
    muu=set()
    a=set(sona)
    for rida in a:
        kordi=sona.count(rida)
        if rida in t:
            tais.add((rida,kordi))
        elif rida in k:
            kaas.add((rida,kordi))
        else:
            muu.add((rida,kordi))
    vastus["Täishäälikud"]=tais
    vastus["Kaashäälikud"]=kaas
    vastus["Muud"]=muu
    return vastus
