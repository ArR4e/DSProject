th=["a", "e", "i", "o", "u", "õ", "ä","ü","ö", "A", "E","I","O","U","Õ","Ä","Ü","Ö"]
m=[" ", "!", ".", "?", ":", ";","-",",","'"]
def erinevad_sümbolid(sõne):
    tähed=set(sõne)
    return tähed
def sümbolite_sagedus(sõne):
    sümbolid={}
    for el in sõne:
        i=sõne.count(el)
        sümbolid[el]=i
    return sümbolid
def grupeeri(sõne):
    vastus={}
    täish=set()
    kaash=set()
    muu=set()
    for el in sõne:
        i=sõne.count(el)
        täht=(el, i)
        if el in th:
            täish.add(täht)
        elif el in m:
            muu.add(täht)
        else:
            kaash.add(täht)
    vastus["Täishäälikud"]=täish
    vastus["Kaashäälikud"]=kaash
    vastus["Muud"]=muu
    return vastus

sõne=input("Sisesta sõne: ")
print(grupeeri(sõne))